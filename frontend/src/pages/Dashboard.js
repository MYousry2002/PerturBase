// src/pages/Dashboard.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer,
  PieChart, Pie, Cell, LineChart, Line, Legend
} from 'recharts';
import './Dashboard.css';

const Dashboard = () => {
  const [summary, setSummary] = useState({});
  const [cellsByExp, setCellsByExp] = useState([]);
  const [featuresByExp, setFeaturesByExp] = useState([]);
  const [mitoByChannel, setMitoByChannel] = useState([]);
  const [riboByChannel, setRiboByChannel] = useState([]);
  const [expTypeDist, setExpTypeDist] = useState([]);

  useEffect(() => {
    api.get('/api/dashboard/summary').then(res => setSummary(res.data));
    api.get('/api/dashboard/cells_by_experiment').then(res => setCellsByExp(res.data));
    api.get('/api/dashboard/features_by_experiment').then(res => setFeaturesByExp(res.data));
    api.get('/api/dashboard/mito_by_channel').then(res => setMitoByChannel(res.data));
    api.get('/api/dashboard/ribo_by_channel').then(res => setRiboByChannel(res.data));
    api.get('/api/dashboard/experiment_type_distribution').then(res => setExpTypeDist(res.data));
  }, []);

  return (
    <div className="dashboard-container">
      <h1>Dashboard</h1>

      {/* Summary Cards */}
      <div className="summary-cards">
        <div className="card"><h3>Total Experiments</h3><p>{summary.total_experiments}</p></div>
        <div className="card"><h3>Total Channels</h3><p>{summary.total_channels}</p></div>
        <div className="card"><h3>Total Cells</h3><p>{summary.total_cells}</p></div>
        <div className="card"><h3>Avg. Features / Channel</h3><p>{summary.avg_features}</p></div>
        <div className="card"><h3>Avg. Mito%</h3><p>{summary.avg_mito}</p></div>
        <div className="card"><h3>Avg. Ribo%</h3><p>{summary.avg_ribo}</p></div>
      </div>

      {/* Charts Section */}
      <div className="chart-section">
        <div className="chart-wrapper">
          <h2>Total Cells by Experiment</h2>
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={cellsByExp} margin={{ top: 20, right: 40, left: 40, bottom: 60 }}>
              <XAxis dataKey="experiment" angle={-25} textAnchor="end" height={80} interval={0} />
              <YAxis />
              <Tooltip />
              <Bar dataKey="total_cells" fill="#1976d2" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-wrapper">
          <h2>Features per Experiment</h2>
          <ResponsiveContainer width="100%" height={400}>
            <LineChart data={featuresByExp} margin={{ top: 20, right: 40, left: 40, bottom: 60 }}>
              <XAxis dataKey="experiment" angle={-25} textAnchor="end" height={80} interval={0} />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="avg_features" stroke="#2e7d32" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-wrapper">
          <h2>Mito Avg by Channel</h2>
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={mitoByChannel} margin={{ top: 20, right: 40, left: 40, bottom: 60 }}>
              <XAxis dataKey="channel" angle={-25} textAnchor="end" height={80} interval={0} />
              <YAxis />
              <Tooltip />
              <Bar dataKey="mito_avg" fill="#f9a825" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-wrapper">
          <h2>Ribo Avg by Channel</h2>
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={riboByChannel} margin={{ top: 20, right: 40, left: 40, bottom: 60 }}>
              <XAxis dataKey="channel" angle={-25} textAnchor="end" height={80} interval={0} />
              <YAxis />
              <Tooltip />
              <Bar dataKey="ribo_avg" fill="#6a1b9a" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-wrapper">
          <h2>Experiment Type Distribution</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                dataKey="count"
                isAnimationActive={false}
                data={expTypeDist}
                cx="50%"
                cy="50%"
                outerRadius={130}
                fill="#8884d8"
                label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
              >
                {expTypeDist.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={['#ff6f61', '#29b6f6', '#81c784'][index % 3]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;