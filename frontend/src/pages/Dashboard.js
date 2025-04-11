// src/pages/Dashboard.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';  // Axios instance with baseURL set to http://127.0.0.1:5000
import './Dashboard.css';

const Dashboard = () => {
  const [metrics, setMetrics] = useState({
    totalExperiments: 0,
    avgQC: 0,
    publishedCount: 0,
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch metrics from the dashboard API endpoint
    api.get('/api/dashboard/metrics')
      .then(response => {
        setMetrics(response.data);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading dashboard metrics...</p>;
  if (error) return <p>Error loading metrics: {error.message}</p>;

  return (
    <div className="dashboard-container">
      <h1>Dashboard</h1>
      <div className="metrics-grid">
        <div className="metric-card">
          <h2>Total Experiments</h2>
          <p>{metrics.totalExperiments}</p>
        </div>
        <div className="metric-card">
          <h2>Average QC Metric</h2>
          {/* Use toFixed(2) to show two decimal places */}
          <p>{metrics.avgQC ? metrics.avgQC.toFixed(2) : 'N/A'}</p>
        </div>
        <div className="metric-card">
          <h2>Published Datasets</h2>
          <p>{metrics.publishedCount}</p>
        </div>
      </div>
      {/* Future enhancement: You can add charts or additional summary panels below */}
    </div>
  );
};

export default Dashboard;