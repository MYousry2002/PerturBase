// src/components/ExperimentList.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import './ExperimentList.css';

const ExperimentList = ({ filters }) => {
  const [experiments, setExperiments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Build query parameters based on filters
    const queryParams = new URLSearchParams(filters).toString();
    const endpoint = `/experiments?${queryParams}`;
    
    api.get(endpoint)
      .then(response => {
        setExperiments(response.data);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, [filters]);

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
                <td>
                  <Link to={`/experiments/${exp.ExpID}`}>{exp.Name}</Link>
                </td>
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