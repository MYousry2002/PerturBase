// src/pages/Experiments.js
import React, { useState } from 'react';
import ExperimentFilter from '../components/forms/ExperimentFilter';
import ExperimentList from '../components/ExperimentList';
import './Experiments.css';

const Experiments = () => {
  const [filters, setFilters] = useState({});

  const handleFilter = (criteria) => {
    setFilters(criteria);
  };

  return (
    <div className="experiments-page">
      <h1>Experiments</h1>
      <ExperimentFilter onFilter={handleFilter} />
      <ExperimentList filters={filters} />
    </div>
  );
};

export default Experiments;