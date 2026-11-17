
# -*- coding: utf-8 -*-
"""

combine_glaes_spider.py

This script joins the outputs from GLAES to the hexagons produced by SPIDER for input to GEOH2.
The inputs are the SPIDER hex.geojson file and the GLAES pv_placements.shp and turbine_placements.shp files.
The output is a hexagon file where a count of turbine and pv installations is attached to the hexagons saved in Data.
"""

import geopandas as gpd
import os
from unidecode import unidecode

# Define country names (used for output filenames)
country_names = [ "United Kingdom"]

# Get path to this file
dirname = os.path.dirname(__file__)

# Create a for loop that can loop through a list of country names
for country_name in country_names:
    print(f"Combining GLAES and SPIDER data for {country_name}!")

    # Clean up country name for file operations
    country_name_clean = unidecode(country_name).replace(" ", "").replace(".", "").replace("'", "")

    # Define file paths
    hex_path = os.path.join(dirname, "Inputs_Spider", "processed", f"{country_name_clean}_hex.geojson")
    wind_path = os.path.join(dirname, "Inputs_Glaes", "processed", f"{country_name}_turbine_placements.shp")
    pv_path = os.path.join(dirname, "Inputs_Glaes", "processed", f"{country_name}_pv_placements.shp")
    save_path = os.path.join(dirname, "Inputs_GeoH2", "Data", f"{country_name_clean}_hex_final.geojson")

    # Load all files
    print(" - Loading files...")
    hex = gpd.read_file(hex_path)
    wind_points = gpd.read_file(wind_path)
    pv_points = gpd.read_file(pv_path)

    # Ensure all data are in the same CRS
    if not hex.crs.equals(pv_points.crs):
        pv_points = pv_points.to_crs(hex.crs)
    if not hex.crs.equals(wind_points.crs):
        wind_points = wind_points.to_crs(hex.crs)

    print(" - Joining turbine locations...")
    spatial_join = gpd.sjoin(wind_points, hex, how='left', predicate='within')
    print("Spatial Join Columns:", spatial_join.columns)

    # Find 'index_right' column dynamically
    index_right_col = next((col for col in spatial_join.columns if col.startswith('index_right')), None)
    if index_right_col:
        wind_point_counts = spatial_join.groupby(index_right_col).size()
        hex['theo_turbines'] = wind_point_counts
        hex['theo_turbines'] = hex['theo_turbines'].fillna(0)
    else:
        print("Error: 'index_right' column not found in spatial join results for turbines.")
        continue

    print(" - Joining PV locations...")
    spatial_join = gpd.sjoin(pv_points, hex, how='left', predicate='within')
    print("Spatial Join Columns:", spatial_join.columns)

    # Find 'index_right' column dynamically
    index_right_col = next((col for col in spatial_join.columns if col.startswith('index_right')), None)
    if index_right_col:
        pv_point_counts = spatial_join.groupby(index_right_col).size()
        hex['theo_pv'] = pv_point_counts
        hex['theo_pv'] = hex['theo_pv'].fillna(0)
    else:
        print("Error: 'index_right' column not found in spatial join results for PVs.")
        continue

    print(" - Done! Saving to GeoJSON...")
    if not hex.empty:
        hex.to_file(save_path, driver='GeoJSON', encoding='utf-8')
        print(" - Save complete!")
    else:
        print(" ! Hex GeoDataFrame is empty. This can happen when your country is much smaller than the hexagon size you have used in Spider. Please use smaller hexagons in Spider and retry. Not saving to GeoJSON.")
