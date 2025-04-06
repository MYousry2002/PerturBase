// src/App.js
import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [experiments, setExperiments] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/experiments')
      .then(res => res.json())
      .then(data => setExperiments(data));
  }, []);

  return (
    <div className="App">
      <h1>PerturbBase</h1>
      <h2>Experiments:</h2>
      <ul>
        {experiments.map(exp => (
          <li key={exp.id}>{exp.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;