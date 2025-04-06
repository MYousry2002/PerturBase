// ExperimentList.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

function ExperimentList() {
  const [experiments, setExperiments] = useState([]);

  useEffect(() => {
    api.get('/api/experiments')
      .then(res => setExperiments(res.data))
      .catch(err => console.error('Failed to fetch experiments:', err));
  }, []);

  return (
    <div>
      <h2>Experiments</h2>
      <ul>
        {experiments.map((exp) => (
          <li key={exp.id}>{exp.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default ExperimentList;