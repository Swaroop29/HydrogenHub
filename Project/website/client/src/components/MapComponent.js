// src/components/MapComponent.js
import React, { useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import { useNavigate } from 'react-router-dom';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// Define the default icon for markers
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

const demandCenters = [
  { name: 'London', coords: [51.5074, -0.1278] },
  { name: 'Manchester', coords: [53.4808, -2.2426] },
  { name: 'Birmingham', coords: [52.4862, -1.8904] },
  { name: 'Glasgow', coords: [55.8642, -4.2518] },
  { name: 'Edinburgh', coords: [55.9533, -3.1883] },
  { name: 'Cardiff', coords: [51.4816, -3.1791] },
  { name: 'Swansea', coords: [51.6214, -3.9436] },
  { name: 'Exeter', coords: [50.7184, -3.5339] }
];

const ChangeView = ({ center, zoom }) => {
  const map = useMap();
  useEffect(() => {
    map.setView(center, zoom);
  }, [center, zoom, map]);
  return null;
};

const MapComponent = ({ center, zoom }) => {
  const navigate = useNavigate();

  const handleMarkerClick = (city) => {
    navigate(`/demand-center/${city}`);
  };

  return (
    <div style={{ height: '100%', width: '100%' }}>
      <MapContainer center={center} zoom={zoom} style={{ height: '100%', width: '100%' }}>
        <ChangeView center={center} zoom={zoom} />
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        {demandCenters.map((center, index) => (
          <Marker
            key={index}
            position={center.coords}
            eventHandlers={{
              click: () => handleMarkerClick(center.name),
            }}
          >
            <Popup>{center.name}</Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
};

export default MapComponent;
