// src/components/ParameterDropdownComponent.js
import React from 'react';

const ParameterDropdownComponent = ({ options, onChange }) => {
  return (
    <select onChange={onChange}>
      <option value="">Select a parameter</option>
      {options.map((option, index) => (
        <option key={index} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  );
};

export default ParameterDropdownComponent;
