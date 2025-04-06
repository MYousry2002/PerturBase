import React from 'react';
import ExperimentList from '../components/ExperimentList';
import './Experiments.css';

const Experiments = () => {
  return (
    <div className="experiments-page">
      <h1>Experiments</h1>
      {/* Additional filtering or controls can be added here */}
      <ExperimentList />
    </div>
  );
};

export default Experiments;