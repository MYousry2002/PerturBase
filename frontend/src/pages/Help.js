// src/pages/Help.js
import React from 'react';
import './Help.css';

const Help = () => {
  return (
    <div className="help-container">
      <h1>Help & Documentation</h1>

      <div className="help-section">
        <h2>📊 Dashboard</h2>
        <p>
          View high-level summaries and visualizations of experiments, including total cell counts, feature averages,
          and experiment types. Use this page for a quick overview of your dataset.
        </p>
      </div>

      <div className="help-section">
        <h2>📁 Experiments</h2>
        <p>
          Browse all available experiments. You can filter by keyword, treatment, date, type, publication status, and more.
          Click on a row to access detailed information about that experiment.
        </p>
      </div>

      <div className="help-section">
        <h2>🧪 Experiment Details</h2>
        <p>
          This page displays full metadata for a selected experiment, including channel-specific summaries (RNA, ADT, sgRNA).
          You can view average statistics, feature summaries, and download associated raw files directly from this page.
          To access this view, select any experiment from the <strong>Experiments</strong> page.
        </p>
      </div>

      <div className="help-section">
        <h2>🔗 Need Help?</h2>
        <p>
          For support or contact information, please refer to the <strong>Home</strong> page, where you’ll find details about the development team.
        </p>
      </div>
    </div>
  );
};

export default Help;