// src/components/DemandCenterPage.js
import React from 'react';
import { useParams } from 'react-router-dom';

const DemandCenterPage = () => {
  const { city } = useParams();

  return (
    <div>
      <h2>{city} - Demand Center</h2>
      <p>Information about {city} goes here.</p>
    </div>
  );
};

export default DemandCenterPage;
