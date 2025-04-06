import React, { useEffect, useState } from 'react';
import api from '../services/api';
import './ExperimentList.css';

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
    <div className="experiment-list-container">
      {experiments.length === 0 ? (
        <p>No experiments found.</p>
      ) : (
        <table className="experiment-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Date</th>
              <th>Treatment</th>
              <th>Source</th>
              <th>Publication</th>
            </tr>
          </thead>
          <tbody>
            {experiments.map(exp => (
              <tr key={exp.ExpID}>
                <td>{exp.ExpID}</td>
                <td>{exp.Name}</td>
                <td>{exp.Date}</td>
                <td>{exp.Treatment}</td>
                <td>{exp.Source}</td>
                <td>{exp.Publication}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default ExperimentList;