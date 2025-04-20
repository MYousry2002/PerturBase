import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      {/* Hero Section */}
      <header className="hero-section">
        <div className="hero-content">
          <img
            src={`${process.env.PUBLIC_URL}/logo.png`}
            alt="PerturBase Logo"
            className="home-logo"
          />
          <h1>PerturBase</h1>
          <p>Your gateway to exploring Perturb‑seq experiments</p>
          <div className="hero-buttons">
            <Link to="/dashboard" className="btn btn-dashboard">
              Data Overview
            </Link>
            <Link to="/experiments" className="btn btn-experiments">
              Experiment Explorer
            </Link>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section className="features-section">
        <h2>Key Features</h2>
        <div className="features-list">
          <div className="feature">
            <h3>Metadata Extraction</h3>
            <p>Automatically parses .rds files to extract essential metadata.</p>
          </div>
          <div className="feature">
            <h3>Advanced Querying</h3>
            <p>Quickly query experiments and cell-level data with ease.</p>
          </div>
          <div className="feature">
            <h3>Interactive Visualizations</h3>
            <p>Visualize data through intuitive charts and graphs.</p>
          </div>
          <div className="feature">
            <h3>Downloadable Results</h3>
            <p>Export query results as CSV files and download visualizations.</p>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="about-section">
        <h2>About PerturBase</h2>
        <p>
          PerturBase is an interactive browser for Perturb‑seq experiment databases, designed to make functional genomics screens more accessible. It empowers both bioinformaticians and experimental biologists to query and visualize large-scale screening data.
         
          For details on how to use the platform, visit the <Link to="/help">Help page</Link>.
        </p>
      </section>

      {/* Developers Section */}
        <section className="developers-section">
        <h2>Developers</h2>

        {/* Top Rectangle: Developer Cards - Horizontally Aligned */}
        <div className="developer-cards-row">
          <div className="developer-card">
            <img src="/students_25/Team10/PerturBase/main/images/yousry.jpg" alt="Mohamed Yousry" />
            <h4>Mohamed Yousry ElSadec</h4>
            <p>Full Stack Developer & Deployment Lead</p>
            <a href="mailto:myousry@bu.edu">myousry@bu.edu</a>
            <a href="https://github.com/myousry2002" target="_blank">GitHub</a>
          </div>
          <div className="developer-card">
            <img src="/students_25/Team10/PerturBase/main/images/luke.jpg" alt="Luke Berger" />
            <h4>Luke Berger</h4>
            <p>Data Pipeline & Database Schema Architect</p>
            <a href="mailto:lukeberg@bu.edu">lukeberg@bu.edu</a>
            <a href="https://github.com/lukeberg" target="_blank">GitHub</a>
          </div>
          <div className="developer-card">
            <img src="/students_25/Team10/PerturBase/main/images/wisdom.jpg" alt="Wisdom Adingo" />
            <h4>Wisdom Adingo</h4>
            <p>User Experience & Data Display Designer</p>
            <a href="mailto:wadingo@bu.edu">wadingo@bu.edu</a>
            <a href="https://github.com/wisdomadingo" target="_blank">GitHub</a>
          </div>
          <div className="developer-card">
            <img src="/students_25/Team10/PerturBase/main/images/shahadat.png" alt="Md Shahadat Hossain" />
            <h4>Md Shahadat Hossain</h4>
            <p>User Experience & Data Display Designer</p>
            <a href="mailto:shahadat@bu.edu">shahadat@bu.edu</a>
            <a href="https://github.com/shahadat4099" target="_blank">GitHub</a>
          </div>
        </div>

        {/* Bottom Rectangle: BU Info - Logo on Left, Text on Right */}
        <div className="bu-info-horizontal">
          <img src="/students_25/Team10/PerturBase/main/images/BUlogo.png" alt="Boston University Logo" className="bu-logo" />
          <div className="bu-text">
          <p>
            This project was developed at <strong>Boston University</strong> as part of <strong>BF768 – Biological Databases Analysis</strong> during the Spring of 2025, under the instruction of <strong>Prof. Gary Benson</strong>. The faculty advisor for this project was <strong>Dr. Brian Cleary</strong>.
          </p>
          </div>
        </div>

        </section>

      {/* Footer */}
      <footer className="home-footer">
        <p>&copy; {new Date().getFullYear()} PerturBase. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Home;