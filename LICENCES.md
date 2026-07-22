# Licences and Attribution

This file covers the deployable `dist/` package for The Food Gap v1.0.0.

## Application Code and Design

The Food Gap application code, copy, and generated share assets in this repository are project assets
for this site. Keep source-data attributions below with any public deployment or redistribution.

## MapLibre GL JS

Vendored files:

- `maplibre-gl.js`
- `maplibre-gl.css`

Version: MapLibre GL JS 4.7.1
Licence: BSD 3-Clause
Upstream licence text: `https://github.com/maplibre/maplibre-gl-js/blob/v4.7.1/LICENSE.txt`

BSD 3-Clause License

Copyright (c) 2023, MapLibre contributors

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and
   the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
   and the following disclaimer in the documentation and/or other materials provided with the
   distribution.

3. Neither the name of MapLibre GL JS nor the names of its contributors may be used to endorse or
   promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Statistics Canada Data

Statistics Canada source terms: `https://www.statcan.gc.ca/en/terms-conditions/open-licence`

The site adapts non-confidential Statistics Canada information. The in-app source notice states that
the work is adapted from Statistics Canada data under the Statistics Canada Open Licence and that it
does not constitute an endorsement by Statistics Canada.

Statistics Canada sources used:

- Census of Population 2021, table 98-10-0103-01: low-income status by age and gender.
- Census of Population 2021, French table 98-10-0103-01 CSV: French census-division labels.
- Census of Population 2021, table 98-10-0057-01: household income statistics.
- Census of Population 2021, table 98-10-0002-01: population and dwelling counts.
- Statistics Canada 2021 cartographic boundary file, census divisions.
- Survey of Household Spending, table 11-10-0125-01.
- Survey of Household Spending, table 11-10-0233-01.
- Monthly average retail prices for selected products, table 18-10-0245-01.

## Northwest Territories Data Citation

NWT Bureau of Statistics, Community Price Index:
`https://www.statsnwt.ca/prices-expenditures/community-price-index/`

The current build uses NWT community food-index values to derive contextual lettuce-price estimates
for Northwest Territories census divisions. See `DATA_SOURCES.md` for the verification notes and local
source-file hash.

## Nunavut Data Citation

2025 Nunavut Food Price Survey regional basket values, as recorded in the local evidence file:
`https://lenunavoix.ca/2026/04/28/au-nunavut-le-cout-de-lalimentation-pese-lourd-sur-les-menages/`

This is treated as secondary evidence in the current build. Replace it with an official Government of
Nunavut survey file if one is obtained before formal publication.

## OpenStreetMap and CARTO Basemap

The remote basemap is served from CARTO raster tiles and is based on OpenStreetMap data.

Required public attribution is shown in the map interface:

- OpenStreetMap: `https://www.openstreetmap.org/copyright`
- CARTO: `https://carto.com/attribution/`

The data layer remains functional without the remote basemap.

## No Endorsement

Use of third-party data, map tiles, or software does not imply endorsement of The Food Gap by
Statistics Canada, MapLibre, OpenStreetMap contributors, CARTO, the NWT Bureau of Statistics, or any
Nunavut data publisher.
