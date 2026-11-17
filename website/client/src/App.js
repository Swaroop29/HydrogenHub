// // src/App.js
// import React, { useState } from 'react';
// import './App.css';
// import MapComponent from './components/MapComponent';
// import GoogleMapComponent from './components/GoogleMapComponent';
// import DropdownComponent from './components/DropdownComponent';
// import ParameterButtonsComponent from './components/ParameterButtonsComponent';
// import DemandCenterPage from './components/DemandCenterPage';
// import { Routes, Route } from 'react-router-dom';

// function App() {
//   const [mapCenter, setMapCenter] = useState([54.5, -3.5]);
//   const [mapZoom, setMapZoom] = useState(6);
//   const [selectedParameter, setSelectedParameter] = useState('');
//   const [mapType, setMapType] = useState('leaflet'); // Add mapType state

//   const handleCountryChange = (event) => {
//     const selectedCountry = event.target.value;

//     switch (selectedCountry) {
//       case 'england':
//         setMapCenter([52.3555, -1.1743]);
//         setMapZoom(7);
//         break;
//       case 'scotland':
//         setMapCenter([56.4907, -4.2026]);
//         setMapZoom(7);
//         break;
//       case 'wales':
//         setMapCenter([51.807, -3.7837]);
//         setMapZoom(9);
//         break;
//       default:
//         setMapCenter([54.5, -3.5]);
//         setMapZoom(5);
//     }
//   };

//   const handleParameterClick = (value) => {
//     setSelectedParameter(value);
//   };

//   const handleMapTypeChange = (event) => {
//     setMapType(event.target.value);
//   };

//   const countryOptions = [
//     { value: '', label: 'Select a country' },
//     { value: 'england', label: 'England' },
//     { value: 'scotland', label: 'Scotland' },
//     { value: 'wales', label: 'Wales' }
//   ];

//   const parameterOptions = [
//     { value: 'road-construction-costs', label: 'Road Construction Costs' },
//     { value: 'trucking-transport-costs', label: 'Trucking Transport Costs' },
//     { value: 'pipeline-transport-costs', label: 'Pipeline Transport Costs' },
//     { value: 'production-costs', label: 'Production Costs' },
//     { value: 'battery-costs', label: 'Battery Costs' },
//     { value: 'solar-costs', label: 'Solar Costs' },
//   ];

//   const demandCenters = [
//     { name: 'London', coords: [51.5074, -0.1278] },
//     { name: 'Manchester', coords: [53.4808, -2.2426] },
//     { name: 'Birmingham', coords: [52.4862, -1.8904] },
//     { name: 'Glasgow', coords: [55.8642, -4.2518] },
//     { name: 'Edinburgh', coords: [55.9533, -3.1883] },
//     { name: 'Cardiff', coords: [51.4816, -3.1791] },
//     { name: 'Swansea', coords: [51.6214, -3.9436] },
//     { name: 'Exeter', coords: [50.7184, -3.5339] }
//   ];

//   return (
//     <div className="App">
//       <div className="map-container">
//         {mapType === 'leaflet' ? (
//           <MapComponent center={mapCenter} zoom={mapZoom} />
//         ) : (
//           <GoogleMapComponent center={mapCenter} zoom={mapZoom} demandCenters={demandCenters} />
//         )}
//       </div>
//       <div className="sidebar">
//         <header className="App-header">
//           <h1>Green Hydrogen in UK</h1>
//           <DropdownComponent options={countryOptions} onChange={handleCountryChange} />
//           <select value={mapType} onChange={handleMapTypeChange}>
//             <option value="leaflet">Leaflet</option>
//             <option value="google">Google Maps</option>
//           </select>
//           <h2>Parameters</h2>
//           <ParameterButtonsComponent options={parameterOptions} onClick={handleParameterClick} />
//           <p>Selected Parameter: {selectedParameter}</p>
         
//         </header>
//         <Routes>
//           <Route path="/demand-center/:city" element={<DemandCenterPage />} />
//         </Routes>
//       </div>
//     </div>
//   );
// }

// export default App;
// src/App.js
import React, { useState } from 'react';
import './App.css';
import MapComponent from './components/MapComponent';
import GoogleMapComponent from './components/GoogleMapComponent';
import DropdownComponent from './components/DropdownComponent';
import ParameterButtonsComponent from './components/ParameterButtonsComponent';
import DemandCenterPage from './components/DemandCenterPage';
import { Routes, Route } from 'react-router-dom';

function App() {
  const [mapCenter, setMapCenter] = useState([54.5, -3.5]);
  const [mapZoom, setMapZoom] = useState(6);
  const [selectedParameter, setSelectedParameter] = useState('');
  const [mapType, setMapType] = useState('leaflet');
  const [currentImageIndex, setCurrentImageIndex] = useState(null);

  const handleCountryChange = (event) => {
    const selectedCountry = event.target.value;

    switch (selectedCountry) {
      case 'england':
        setMapCenter([52.3555, -1.1743]);
        setMapZoom(7);
        break;
      case 'scotland':
        setMapCenter([56.4907, -4.2026]);
        setMapZoom(7);
        break;
      case 'wales':
        setMapCenter([51.807, -3.7837]);
        setMapZoom(9);
        break;
      default:
        setMapCenter([54.5, -3.5]);
        setMapZoom(5);
    }
  };

  const handleParameterClick = (value) => {
    setSelectedParameter(value);
    setCurrentImageIndex(parameterOptions.findIndex(option => option.value === value));
  };

  const handleMapTypeChange = (event) => {
    setMapType(event.target.value);
  };

  const handleClose = () => {
    setSelectedParameter('');
    setCurrentImageIndex(null);
  };

  const handleNext = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex + 1) % parameterOptions.length);
  };

  const handlePrev = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex - 1 + parameterOptions.length) % parameterOptions.length);
  };

  const countryOptions = [
    { value: '', label: 'Select a country' },
    { value: 'england', label: 'England' },
    { value: 'scotland', label: 'Scotland' },
    { value: 'wales', label: 'Wales' }
  ];

  const parameterOptions = [
    { value: 'road-construction-costs', label: 'Road Construction Costs' },
    { value: 'trucking-transport-costs', label: 'Trucking Transport Costs' },
    { value: 'pipeline-transport-costs', label: 'Pipeline Transport Costs' },
    { value: 'production-costs', label: 'Production Costs' },
    { value: 'battery-costs', label: 'Battery Costs' },
    { value: 'solar-costs', label: 'Solar Costs' },
  ];

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

  return (
    <div className="App">
      <div className="map-container">
        {mapType === 'leaflet' ? (
          <MapComponent center={mapCenter} zoom={mapZoom} />
        ) : (
          <GoogleMapComponent center={mapCenter} zoom={mapZoom} demandCenters={demandCenters} />
        )}
      </div>
      <div className="sidebar">
        <header className="App-header">
          <h1>Green Hydrogen in UK</h1>
          <DropdownComponent options={countryOptions} onChange={handleCountryChange} />
          <select value={mapType} onChange={handleMapTypeChange}>
            <option value="leaflet">Leaflet</option>
            <option value="google">Google Maps</option>
          </select>
          <h2>Parameters</h2>
          <ParameterButtonsComponent options={parameterOptions} onClick={handleParameterClick} />
          <p>Selected Parameter: {selectedParameter}</p>
          {selectedParameter && (
            <div className="overlay">
              <div className="graph-container">
                <button className="close-btn" onClick={handleClose}>×</button>
                <button className="prev-btn" onClick={handlePrev}>←</button>
                <button className="next-btn" onClick={handleNext}>→</button>
                {parameterOptions[currentImageIndex] && (
                  <img
                    src={`/graphs/${parameterOptions[currentImageIndex].value}.png`}
                    alt={parameterOptions[currentImageIndex].label}
                  />
                )}
              </div>
            </div>
          )}
        </header>
        <Routes>
          <Route path="/demand-center/:city" element={<DemandCenterPage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
