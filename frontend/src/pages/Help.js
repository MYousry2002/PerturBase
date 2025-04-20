// src/pages/Help.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Help.css';

const Help = () => {
  return (
    <div className="help-container">
      <h1>Help & Documentation</h1>

      {/* Dashboard Section */}
      <div className="help-section">
        <h2>📊 Dashboard</h2>
        <p>
          The dashboard offers a high-level overview of all experiments in PerturBase. It summarizes total cell counts,
          average features, gene counts, and experiment types using visualizations. Use this page to quickly assess the dataset
          and explore global trends before diving into individual experiments.
        </p>
      </div>

      {/* Experiments Section */}
      <div className="help-section">
        <h2>📁 Experiments</h2>
        <p>
          The Experiments page lists all available perturb-seq screens. You can filter by treatment, date, type,
          publication status, and more. Clicking on any experiment takes you to its detailed view. This page is
          ideal for discovering and navigating through available datasets.
        </p>
      </div>

      {/* Experiment Details Section */}
      <div className="help-section">
        <h2>🧪 Experiment Details</h2>
        <p>
          Each experiment has its own detail page, structured into three tabs:
        </p>
        <ul>
          <li><strong>Metadata:</strong> View experiment-level metadata like treatment, date, source, and publication info. Below that, you’ll find a summary table of all channels (e.g., RNA, ADT, sgRNA) showing average cell and feature metrics.</li>
          <li><strong>Visualization:</strong> Browse static plots across four views: <em>Metrics</em>, <em>Umap</em>, <em>Top Genes</em>, and <em>Heatmap</em>. Use the built-in image carousel to scroll through available plots, and download them individually using the download icon in the corner.</li>
          <li><strong>Download:</strong> Download the full raw data files for the experiment, including metadata and count matrices.</li>
        </ul>
      </div>

      {/* Help Section */}
      <div className="help-section">
        <h2>🔗 Need More Help?</h2>
        <p>
          For support, feedback, or questions, visit the <Link to="/">Home</Link> page. There you'll find contact details and GitHub profiles
          for the developers behind PerturBase. Feel free to reach out directly by email or submit issues through GitHub.
        </p>
      </div>
    </div>
  );
};

export default Help;