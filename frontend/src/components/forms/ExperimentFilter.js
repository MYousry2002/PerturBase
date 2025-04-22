// src/components/forms/ExperimentFilter.js
import React, { useState, useEffect } from 'react';
import api from '../../services/api';
import './ExperimentFilter.css';

const ExperimentFilter = ({ onFilter }) => {
  const [keyword, setKeyword] = useState('');
  const [treatment, setTreatment] = useState('');
  const [publication, setPublication] = useState('');
  const [expType, setExpType] = useState('');
  const [minCells, setMinCells] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [source, setSource] = useState('');
  const [showAdvanced, setShowAdvanced] = useState(false);

  const toggleAdvanced = () => {
    setShowAdvanced(prev => !prev);
  };

  const [treatmentOptions, setTreatmentOptions] = useState([]);
  const [sourceOptions, setSourceOptions] = useState([]);
  const [publicationOptions, setPublicationOptions] = useState([]);

  useEffect(() => {
    api.get('/api/experiments/distinct_values')
      .then(res => {
        setTreatmentOptions(res.data.treatments || []);
        setSourceOptions(res.data.sources || []);
        setPublicationOptions(res.data.publications || []);
      })
      .catch(err => console.error('Error fetching dropdown values:', err));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    onFilter({
      keyword,
      treatment,
      publication,
      type: expType,
      min_cells: minCells,
      start_date: startDate,
      end_date: endDate,
      source
    });
  };

  const handleReset = () => {
    setKeyword('');
    setTreatment('');
    setPublication('');
    setExpType('');
    setMinCells('');
    setStartDate('');
    setEndDate('');
    setSource('');
    setShowAdvanced(false);
    onFilter({});
  };

  return (
    <form className="experiment-filter" onSubmit={handleSubmit}>
      {/* Primary Filters */}
      <div className="filter-group">
        <label htmlFor="keyword">Keyword</label>
        <input
          id="keyword"
          type="text"
          placeholder="Search by name"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
        />
      </div>

      <div className="filter-group">
        <label htmlFor="treatment">Treatment</label>
        <input
          id="treatment"
          list="treatment-options"
          placeholder="Choose or type"
          value={treatment}
          onChange={(e) => setTreatment(e.target.value)}
        />
        <datalist id="treatment-options">
          {treatmentOptions.map((val, idx) => (
            <option key={idx} value={val} />
          ))}
        </datalist>
      </div>

      <div className="filter-group">
        <label htmlFor="type">Experiment Type</label>
        <select
          id="type"
          value={expType}
          onChange={(e) => setExpType(e.target.value)}
        >
          <option value="">Any</option>
          <option value="RNA">RNA</option>
          <option value="ADT">ADT</option>
          <option value="sgRNA">sgRNA</option>
        </select>
      </div>

      <div className="filter-group">
        <label htmlFor="minCells">Min Cells</label>
        <input
          id="minCells"
          type="number"
          placeholder="e.g., 10000"
          value={minCells}
          onChange={(e) => setMinCells(e.target.value)}
        />
      </div>

      {showAdvanced && (
        <div className="advanced-section">
          <div className="filter-group">
            <label htmlFor="publication">Publication</label>
            <input
              id="publication"
              list="publication-options"
              placeholder="Enter DOI or Unpublished"
              value={publication}
              onChange={(e) => setPublication(e.target.value)}
            />
            <datalist id="publication-options">
              {publicationOptions.map((val, idx) => (
                <option key={idx} value={val} />
              ))}
            </datalist>
          </div>

          <div className="filter-group">
            <label htmlFor="source">Source</label>
            <input
              id="source"
              list="source-options"
              placeholder="Choose or type"
              value={source}
              onChange={(e) => setSource(e.target.value)}
            />
            <datalist id="source-options">
              {sourceOptions.map((val, idx) => (
                <option key={idx} value={val} />
              ))}
            </datalist>
          </div>

          <div className="filter-group">
            <label htmlFor="startDate">Start Date</label>
            <input
              id="startDate"
              type="date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
            />
          </div>

          <div className="filter-group">
            <label htmlFor="endDate">End Date</label>
            <input
              id="endDate"
              type="date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
            />
          </div>
        </div>
      )}

      <div className="toggle-wrapper">
        <button
          type="button"
          onClick={toggleAdvanced}
          className={`toggle-btn ${showAdvanced ? 'active' : ''}`}
        >
          {showAdvanced ? 'Hide Advanced Filters' : 'Show Advanced Filters'}
          <div className="arrow-container">
            <svg
              className={`arrow-icon ${showAdvanced ? 'rotate' : ''}`}
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              width="22"
              height="22"
            >
              <path d="M7 10l5 5 5-5z" fill="currentColor" />
            </svg>
          </div>
        </button>
      </div>
      
      <div className="filter-actions">
        <button type="submit" className="btn-filter">Apply Filters</button>
        <button type="button" className="btn-reset" onClick={handleReset}>Reset</button>
      </div>
    </form>
  );
};

export default ExperimentFilter;