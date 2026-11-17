// src/components/DropdownComponent.js
import React from 'react';
import './DropdownComponent.css';

const DropdownComponent = ({ options, onChange, className }) => {
  return (
    <select className={`dropdown ${className}`} onChange={onChange}>
      {options.map((option) => (
        <option key={option.value} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  );
};

export default DropdownComponent;
