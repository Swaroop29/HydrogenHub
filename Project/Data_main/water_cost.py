
"""
Water costs for hydrogen production in each hexagon
"""

import geopandas as gpd
import pandas as pd
import numpy as np

# Load the hexagon data
hexagons = gpd.read_file('Resources/hex_lcoh.geojson')

# Load technology and country parameters
technology_parameters = "Parameters/technology_parameters.xlsx"
country_excel_path = 'Parameters/country_parameters.xlsx'

water_data = pd.read_excel(technology_parameters,
                           sheet_name='Water',
                           index_col='Parameter').squeeze("columns")
country_parameters = pd.read_excel(country_excel_path,
                                   index_col='Country')

# Initialize arrays for water costs
h2o_costs_dom_water_bodies = np.empty(len(hexagons))
h2o_costs_ocean = np.empty(len(hexagons))
h2o_costs = np.empty(len(hexagons))

# Extract necessary parameters from the data
electricity_demand_h2o_treatment = water_data['Freshwater treatment electricity demand (kWh/m3)']
electricity_demand_h2o_ocean_treatment = water_data['Ocean water treatment electricity demand (kWh/m3)']
water_transport_costs = water_data['Water transport cost (pounds/100 km/m3)']
water_spec_cost = water_data['Water specific cost (pounds/m3)']
water_demand = water_data['Water demand (L/kg H2)']

# Function to get the correct column name based on the country
def get_distance_column(country, type):
    if country == 'UnitedKingdom':
        prefix = 'england'
    elif country == 'Scotland':
        prefix = 'scotland'
    elif country == 'Wales':
        prefix = 'wales'
    else:
        raise ValueError(f"Unexpected country: {country}")
    return f'{prefix}_{type}_dist'

# Calculate water costs for each hexagon
for i in range(len(hexagons)):
    country = hexagons.at[i, 'country']
    waterbody_dist_col = get_distance_column(country, 'waterbody')
    waterway_dist_col = get_distance_column(country, 'waterway')
    
    h2o_costs_dom_water_bodies[i] = (water_spec_cost 
                                     + (water_transport_costs/100) * min(hexagons.at[i, waterbody_dist_col],
                                                                         hexagons.at[i, waterway_dist_col])
                                     + electricity_demand_h2o_treatment * country_parameters.at[country, 'Electricity price (pounds/kWh)']
                                     ) * water_demand / 1000
    
    h2o_costs_ocean[i] = (water_spec_cost 
                          + (water_transport_costs/100) * hexagons.at[i, 'ocean_dist']
                          + electricity_demand_h2o_ocean_treatment * country_parameters.at[country, 'Electricity price (pounds/kWh)']
                          ) * water_demand / 1000
    
    h2o_costs[i] = min(h2o_costs_dom_water_bodies[i], h2o_costs_ocean[i])

# Add the calculated water costs to the hexagons GeoDataFrame
hexagons['Ocean water costs'] = h2o_costs_ocean
hexagons['Freshwater costs'] = h2o_costs_dom_water_bodies
hexagons['Lowest water cost'] = h2o_costs

# Save the updated GeoDataFrame to a new GeoJSON file
hexagons.to_file('Resources/hex_water.geojson', driver='GeoJSON', encoding='utf-8')
