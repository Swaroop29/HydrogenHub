// src/components/GoogleMapComponent.js
import React, { useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

// Define the default container style
const containerStyle = {
  width: '100%',
  height: '100%'
};

// Define map types for Google Maps
const mapTypes = {
  ROADMAP: 'roadmap',
  SATELLITE: 'satellite',
  HYBRID: 'hybrid',
  TERRAIN: 'terrain'
};

const GoogleMapComponent = ({ center, zoom, demandCenters }) => {
  const [mapType, setMapType] = useState(mapTypes.ROADMAP);

  const handleMapTypeChange = (event) => {
    setMapType(event.target.value);
  };

  return (
    <div style={{ height: '100%', width: '100%', position: 'relative' }}>
      <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}>
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={{ lat: center[0], lng: center[1] }}
          zoom={zoom}
          mapTypeId={mapType}
        >
          {/* Render dynamic markers */}
          {demandCenters.map((center, index) => (
            <Marker
              key={index}
              position={{ lat: center.coords[0], lng: center.coords[1] }}
              label={center.name}
            />
          ))}
        </GoogleMap>
      </LoadScript>
     </div>
  );
};

export default GoogleMapComponent;
