// src/components/ParameterButtonsComponent.js
import React from 'react';
import './ParameterButtonsComponent.css'; // Optional: Create CSS file for styling

function ParameterButtonsComponent({ options, onClick }) {
  return (
    <div className="parameter-buttons">
      {options.map((option) => (
        <button 
          key={option.value}
          onClick={() => onClick(option.value)}
          className="parameter-button"
        >
          {option.label}
        </button>
      ))}
    </div>
  );
}

export default ParameterButtonsComponent;
