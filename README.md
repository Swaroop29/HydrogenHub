# HydrogenHub

**Where is green hydrogen cheapest to make and deliver in the UK?**

HydrogenHub is a geospatial cost model and interactive map for green hydrogen supply in the United Kingdom. It finds the lowest-cost place to produce hydrogen from wind and solar, and the cheapest way to deliver it as liquid hydrogen (LH2) to eight demand centres: London, Birmingham, Manchester, Edinburgh, Glasgow, Swansea, Cardiff and Exeter.

> **Report:** Patil, S. (2024). _Green Hydrogen Model: Geospatial Cost Optimization and Visualization for the United Kingdom._ Zenodo. https://zenodo.org/records/24286217

![London LH2 trucking LCOH map](<Project/Data_main/Resources/UK/London LH2 trucking LCOH.png>)

_Levelised cost of delivering liquid hydrogen to London by truck, for each hexagon where it could be produced (€/kg)._

---

## What it does

The UK is divided into **1,026 hexagonal cells** (H3 grid). For every cell and every demand centre, the model:

1. **Designs a hydrogen plant.** It sizes wind, solar, battery, electrolyser and hydrogen storage to meet the demand profile, using a full year (2023) of hourly ERA5 weather data.
2. **Optimises delivery.** It compares trucking (including new road construction where needed) with pipelines, including liquefaction.
3. **Adds water costs** for freshwater or ocean-water supply.
4. **Reports the levelised cost of hydrogen (LCOH)** per cell and per demand centre, broken down by component.

The model builds on the open-source [GeoH2](https://github.com/ClimateCompatibleGrowth/GeoH2) framework (Halloran et al., 2024), applied here to the UK, and uses [GLAES](https://github.com/FZJ-IEK3-VSA/glaes) for land eligibility and [Spider](https://github.com/carderne/ccg-spider) for the hexagon grid.

## Key results

| Demand centre | Lowest delivered cost (€/kg LH2) | Production at best site (€/kg) | Transport and conversion (€/kg) |
| --- | --- | --- | --- |
| London | 18.26 | 5.00 | 13.23 |
| Birmingham | 19.51 | 5.01 | 14.48 |
| Manchester | 22.51 | 5.03 | 17.46 |
| Edinburgh | 23.57 | 5.03 | 18.52 |
| Glasgow | 25.32 | 5.04 | 20.26 |
| Swansea | 31.13 | 5.06 | 26.04 |
| Cardiff | 33.75 | 5.08 | 28.64 |
| Exeter | 37.00 | 5.10 | 31.88 |

- **Delivery, not production, drives cost.** Production is about €5/kg at the best site and varies little. Transport and conversion make up 72 to 86 per cent of the delivered cost.
- **One site wins for every city.** The same coastal hexagon (`85195a2bfffffff`) is the cheapest place to produce hydrogen for all eight demand centres.
- **Trucking usually beats pipelines**, in 59 to 73 per cent of cells, though the margin is small.
- **Water is negligible**, at about €0.02 to €0.05/kg.

![London LH2 trucking production cost map](<Project/Data_main/Resources/UK/London LH2 trucking production cost.png>)

_Production cost alone (€/kg). It varies far less across the UK than delivered cost does._

All costs are in euros. The parameter spreadsheets mix euro-based hardware costs inherited from GeoH2 with pound-based energy and water prices, so treat the figures as indicative.

Maps and charts for every demand centre are in [`Project/Data_main/Resources/UK`](Project/Data_main/Resources/UK). The cell-level result files are in [`Project/Data_main/Resources`](Project/Data_main/Resources).

## Repository layout

```
Project/
  Data_prep/   Builds the spatial inputs (land eligibility, hexagon grid, distances)
  glaes/       GLAES land-eligibility tool and workflow
  Spider/      Spider hexagon-grid configuration
  Data_main/   The cost model, its parameters, and the results
    Parameters/   Excel and CSV inputs (demand, costs, weather, transport, ...)
    Resources/    Model outputs: GeoJSON, CSV and map images
website/
  client/      React front end (interactive map)
  server.js    Express server
```

## How to run

### Option A: view the website

Requires [Node.js](https://nodejs.org/).

```bash
cd website
npm install
npm install --prefix client
```

Create `website/client/.env` with a Google Maps API key:

```
REACT_APP_GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
```

Then start the app:

```bash
npm run dev
```

The React client opens on http://localhost:3000 and the Express server runs on port 5000.

### Option B: re-run the analysis

1. **Prepare the data.** Follow [`Project/Data_prep/README.md`](Project/Data_prep/README.md). In short, download the raw spatial data (Natural Earth countries, Marine Regions, OpenStreetMap, Corine land cover), run `spatial_data_prep.py`, run GLAES and Spider, then run `combine_glaes_spider.py`.
2. **Set up the model environment.**
   ```bash
   cd Project/Data_main
   mamba env create -f environment.yaml
   mamba activate model
   ```
   You also need a [Copernicus CDS API key](https://cds.climate.copernicus.eu/api-how-to) for the weather download, and an optimisation solver such as Cbc or Gurobi.
3. **Run the pipeline in order.**
   ```bash
   python assign_country.py
   python get_weather_data.py
   python optimize_transport_and_conversion.py
   python optimize_hydrogen_plant.py
   python water_cost.py
   python total_hydrogen_cost.py
   python costs_by_component.py
   python map_costs.py
   ```
   The plant optimisation can take from several minutes to several hours. See [`Project/Data_main/README.md`](Project/Data_main/README.md) for details.

Demand centres, prices, interest rates and technology assumptions are all set in the spreadsheets in `Project/Data_main/Parameters`.

## Limitations

- Only new wind and solar plants are modelled. Grid electricity and existing generation are excluded, and all excess electricity is curtailed.
- Each demand centre is served by its own plant, with no shared economies of scale.
- Truck selection is greedy, not globally optimal. Terrain is ignored in road and pipeline costs.
- Water supply is unconstrained, and one year of weather data is used.
- The results have not been sensitivity-tested or validated against external UK cost estimates.

## Citation

If you use this work, please also cite the underlying model:

> Halloran, C., Leonard, A., Salmon, N., Müller, L., & Hirmer, S. (2024). GeoH2 model: Geospatial cost optimization of green hydrogen production including storage and transportation. _MethodsX_, 12, 102660. https://doi.org/10.1016/j.mex.2024.102660

## License

The GeoH2-derived code keeps its original licence; see `Project/Data_main/LICENSE`. GLAES and Spider carry their own licences in their folders.
