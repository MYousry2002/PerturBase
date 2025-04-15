// src/components/ExperimentList.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';
import './ExperimentList.css';

const ExperimentList = ({ filters }) => {
  const [experiments, setExperiments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [sortBy, setSortBy] = useState('ExpID');
  const [sortOrder, setSortOrder] = useState('ASC');

  useEffect(() => {
    const queryParams = new URLSearchParams({
      ...filters,
      sort_by: sortBy,
      sort_order: sortOrder
    }).toString();

    api.get(`/api/experiments?${queryParams}`)
      .then(response => {
        if (!Array.isArray(response.data)) {
          throw new Error(`Expected an array but got ${typeof response.data}`);
        }
        setExperiments(response.data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching experiments:', err);
        setError(err);
        setLoading(false);
      });
  }, [filters, sortBy, sortOrder]);

  const handleSort = (field) => {
    if (sortBy === field) {
      setSortOrder(prev => (prev === 'ASC' ? 'DESC' : 'ASC'));
    } else {
      setSortBy(field);
      setSortOrder('ASC');
    }
  };

  const renderSortArrow = (field) => {
    if (sortBy === field) {
      return sortOrder === 'ASC' ? '▲' : '▼';
    }
    return '△'; // double arrow when not active
  };

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
              <th
                onClick={() => handleSort('ExpID')}
                className={`sortable-header ${sortBy === 'ExpID' ? 'active' : ''}`}
              >
                ID <span className="sort-arrow">{renderSortArrow('ExpID')}</span>
              </th>
              <th>Name</th>
              <th
                onClick={() => handleSort('Date')}
                className={`sortable-header ${sortBy === 'Date' ? 'active' : ''}`}
              >
                Date <span className="sort-arrow">{renderSortArrow('Date')}</span>
              </th>
              <th>Treatment</th>
              <th>Source</th>
              <th>Publication</th>
              <th>Type</th>
              <th>Total Cells</th>
              <th># Channels</th>
            </tr>
          </thead>
          <tbody>
            {experiments.map(exp => (
              <tr key={exp.ExpID}>
                <td>{exp.ExpID}</td>
                <td><Link to={`/experiments/${exp.ExpID}`}>{exp.Name}</Link></td>
                <td>{exp.Date}</td>
                <td>{exp.Treatment}</td>
                <td>{exp.Source}</td>
                <td>{exp.Publication}</td>
                <td>{exp.Type}</td>
                <td>{exp.TotalCells ?? 0}</td>
                <td>{exp.NumChannels ?? 0}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default ExperimentList;