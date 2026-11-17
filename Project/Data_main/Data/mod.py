import json

# Load your GeoJSON data (if needed)
with open('hexagons_with_country.geojson', 'r') as file:
    data = json.load(file)

# Iterate over each feature
for feature in data['features']:
    # Ensure 'properties' key exists
    if 'properties' not in feature:
        feature['properties'] = {}
    
    # Add or update the 'country' key
    feature['properties']['country'] = 'UnitedKingdom'

# Save the updated GeoJSON data (if needed)
with open('hexagons_with_country.geojson', 'w') as file:
    json.dump(data, file, indent=4)
