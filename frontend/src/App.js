// src/App.js

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Experiments from './pages/Experiments';
import Experiment from './pages/Experiment';
import Help from './pages/Help';
import Navbar from './components/common/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/experiments" element={<Experiments />} />
        <Route path="/experiments/:expId" element={<Experiment />} />
        <Route path="/help" element={<Help />} />
      </Routes>
    </Router>
  );
}

export default App;