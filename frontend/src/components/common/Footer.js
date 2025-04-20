// src/components/common/Footer.js
import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="app-footer">
      <p>&copy; {new Date().getFullYear()} PerturBase. All rights reserved.</p>
    </footer>
  );
};

export default Footer;