import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; // Import the CSS for Home styling

function Home() {
  return (
    <div className="home-container">
      {/* Hero Section */}
      <header className="hero-section">
        <div className="hero-content">
          <h1>PerturBase</h1>
          <p>Your gateway to exploring Perturb-seq experiments</p>
          <Link to="/dashboard" className="btn btn-primary">
            Explore Dashboard
          </Link>
        </div>
      </header>

      {/* Features Section */}
      <section className="features-section">
        <h2>Features</h2>
        <div className="features-list">
          <div className="feature">
            <h3>Metadata Extraction</h3>
            <p>Automatically parses .rds files to extract key metadata.</p>
          </div>
          <div className="feature">
            <h3>Advanced Querying</h3>
            <p>Quickly query experiments and cell-level data.</p>
          </div>
          <div className="feature">
            <h3>Visualizations</h3>
            <p>Intuitive charts and graphs to help you explore your data.</p>
          </div>
          <div className="feature">
            <h3>Downloadable Results</h3>
            <p>Export query results as CSV and download visualizations.</p>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="about-section">
        <h2>About PerturBase</h2>
        <p>
          PerturBase is a web-based platform that makes functional genomics data more accessible.
          It empowers both computational and non-programming users to explore, query, and visualize large-scale
          Perturb-seq experiments using a powerful API and a user-friendly interface.
        </p>
      </section>

      {/* Footer */}
      <footer className="home-footer">
        <p>&copy; {new Date().getFullYear()} PerturBase. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default Home;