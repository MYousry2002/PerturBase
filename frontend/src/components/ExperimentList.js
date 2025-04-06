import React, { useEffect, useState } from 'react';
import api from '../services/api'; // Adjust the path as needed

const ExperimentList = () => {
  const [experiments, setExperiments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Access the "experiments" endpoint
    api.get('/experiments')
      .then(response => {
        setExperiments(response.data);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading experiments...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <h2>Experiments</h2>
      <ul>
        {experiments.map(exp => (
          <li key={exp.ExpID}>{exp.Name}</li>
        ))}
      </ul>
    </div>
  );
};

export default ExperimentList;