import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <img src={`${process.env.PUBLIC_URL}/logo.png`} alt="PerturBase logo" className="logo-image" />
        <span className="logo-text">PerturBase</span>
      </div>
      <ul className="navbar-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/dashboard">Dashboard</Link></li>
        <li><Link to="/experiments">Experiments</Link></li>
        <li><Link to="/help">Help</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;