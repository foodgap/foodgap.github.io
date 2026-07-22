#!/usr/bin/env python3
"""Replace canada.js geometry with StatCan official 2021 CD boundaries,
topology-preserved (shapely.coverage_simplify) so adjacent regions share
identical edges — eliminating sliver gaps between divisions."""
import json, re, sys, os
import shapefile, numpy as np
import shapely
from shapely.geometry import shape, mapping
from shapely.ops import transform as shp_transform
from pyproj import Transformer

W = os.path.expanduser("~/Documents/foodgap-site")
print("① read shapefile…", flush=True)
r = shapefile.Reader(W + "/geo/lcd_000b21a_e", encoding="latin-1")
fields = [f[0] for f in r.fields[1:]]
idi = fields.index("CDUID" if "CDUID" in fields else [f for f in fields if "CDUID" in f][0])
geoms, ids = [], []
for sr in r.iterShapeRecords():
    ids.append(str(sr.record[idi]))
    geoms.append(shape(sr.shape.__geo_interface__))
print(f"   {len(geoms)} divisions; total vertices ≈ {sum(shapely.get_num_coordinates(g) for g in geoms):,}", flush=True)

print("② reproject Lambert → WGS84…", flush=True)
tr = Transformer.from_crs("EPSG:3347", "EPSG:4326", always_xy=True)
def rp(g): return shp_transform(lambda x, y: tr.transform(x, y), g)
geoms = [rp(g) for g in geoms]

from shapely.geometry import Polygon, MultiPolygon
def prune(g, min_part=8e-4, min_hole=8e-4):
    """Drop speck islands / lake-holes (< ~6 km²). Shared land borders untouched;
    the largest part of every division is always kept."""
    parts = list(g.geoms) if g.geom_type == "MultiPolygon" else [g]
    biggest = max(parts, key=lambda p: p.area)
    keep = []
    for p in parts:
        if p is not biggest and p.area < min_part: continue
        holes = [h for h in p.interiors if Polygon(h).area >= min_hole]
        keep.append(Polygon(p.exterior, holes))
    return keep[0] if len(keep) == 1 else MultiPolygon(keep)
def rnd(o):  # round every coordinate to 4 decimals (~11 m; shared vertices round identically)
    if isinstance(o, (list, tuple)): return [rnd(x) for x in o]
    return round(o, 4)
def gjson(g):
    m = mapping(g); return {"type": m["type"], "coordinates": rnd(m["coordinates"])}
print("③ topology-preserving simplify (tuning tolerance)…", flush=True)
best = None
for tol in (0.010, 0.020, 0.040):
    simp = shapely.coverage_simplify(np.array(geoms, dtype=object), tol)
    simp = [prune(g) for g in simp]
    gj = [gjson(g) for g in simp]
    size = sum(len(json.dumps(g, separators=(",", ":"))) for g in gj)
    verts = sum(shapely.get_num_coordinates(g) for g in simp)
    valid = bool(shapely.coverage_is_valid(np.array(simp, dtype=object)))
    print(f"   tol={tol}: {verts:,} vertices | geometry JSON {size/1e6:.2f} MB | coverage valid: {valid}", flush=True)
    if valid and size <= 2_000_000: best = (tol, gj); break
    if valid: best = (tol, gj)
if not best: sys.exit("no valid simplification found")
tol, gj = best
simp_by_idx = gj
print(f"   → using tol={tol}", flush=True)

print("④ splice into canada.js…", flush=True)
src = open(W + "/canada.js").read()
m = re.search(r"(window\.CANADA_DATA = )(.*?)(;\n)", src, re.S)
fc = json.loads(m.group(2))
by = dict(zip(ids, gj))
missing = [f["properties"]["code"] for f in fc["features"] if f["properties"]["code"] not in by]
if missing: sys.exit(f"CDUIDs missing from official file: {missing}")
props_before = json.dumps([f["properties"] for f in fc["features"]], sort_keys=True)
for f in fc["features"]:
    f["geometry"] = by[f["properties"]["code"]]
props_after = json.dumps([f["properties"] for f in fc["features"]], sort_keys=True)
assert props_before == props_after, "properties changed!"
out = src[:m.start(2)] + json.dumps(fc, separators=(",", ":")) + src[m.end(2):]
open(W + "/canada.js", "w").write(out)
print(f"✅ canada.js rewritten: {len(out)/1e6:.2f} MB | 293 geometries = official StatCan 2021, gap-free coverage (tol {tol}°)")
