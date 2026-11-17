
"""
This script fetches historical weather data to calculate wind and solar potential
from the ERA-5 reanalysis dataset using Atlite.

For this script to work, you must have:
- Installed the `Copernicus Climate Data Store <https://cds.climate.copernicus.eu>`_ ``cdsapi`` package  (`install with `pip``) 
- Registered and set up your CDS API key as described on their website <https://cds.climate.copernicus.eu/api-how-to>
"""

import logging
import atlite
import pandas as pd
import os

logging.basicConfig(level=logging.INFO)

# Path to the single Excel file with multiple sheets
weather_excel_path = "Parameters/weather_parameters.xlsx"
sheet_names = ['UnitedKingdom']

# Create folders for final cutouts and temporary files if they do not exist
if not os.path.exists('Cutouts'):
    os.makedirs('Cutouts')
if not os.path.exists('temp'):
    os.makedirs('temp')

# Loop through each sheet name to process each country's weather parameters
for sheet_name in sheet_names:
    # Read the specific sheet from the Excel file into a pandas Series
    weather_parameters = pd.read_excel(weather_excel_path, sheet_name=sheet_name, index_col='Parameters').squeeze('columns')

    # Extract the parameters from the Series
    start_date = weather_parameters['Start date']
    end_date = weather_parameters['End date (not inclusive)']
    min_lon = weather_parameters['Minimum longitude (deg)']
    max_lon = weather_parameters['Maximum longitude (deg)']
    min_lat = weather_parameters['Minimum latitude (deg)']
    max_lat = weather_parameters['Maximum latitude (deg)']
    filename = weather_parameters['Filename']

    # Define the date range to import, with the end date being non-inclusive
    snapshots = slice(start_date, end_date)

    # Create an Atlite cutout object with the specified parameters
    cutout = atlite.Cutout(
        path="Cutouts/" + filename + ".nc",
        module="era5",
        x=slice(min_lon, max_lon),
        y=slice(min_lat, max_lat),
        time=snapshots,
    )

    # Prepare the cutout and save it to the specified path
    cutout.prepare(tmpdir="temp")  # Use a temporary directory for processing
