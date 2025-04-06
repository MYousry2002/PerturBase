import React, { useState } from 'react';
import './ExperimentFilter.css';

const ExperimentFilter = ({ onFilter }) => {
  const [keyword, setKeyword] = useState('');
  const [treatment, setTreatment] = useState('');
  const [publication, setPublication] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Pass the filter criteria to the parent component
    onFilter({
      keyword,
      treatment,
      publication,
      start_date: startDate,
      end_date: endDate,
    });
  };

  const handleReset = () => {
    setKeyword('');
    setTreatment('');
    setPublication('');
    setStartDate('');
    setEndDate('');
    onFilter({});
  };

  return (
    <form className="experiment-filter" onSubmit={handleSubmit}>
      <div className="filter-group">
        <label htmlFor="keyword">Keyword:</label>
        <input
          id="keyword"
          type="text"
          placeholder="Search by Name"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
        />
      </div>

      <div className="filter-group">
        <label htmlFor="treatment">Treatment:</label>
        <input
          id="treatment"
          type="text"
          placeholder="Control, etc."
          value={treatment}
          onChange={(e) => setTreatment(e.target.value)}
        />
      </div>

      <div className="filter-group">
        <label htmlFor="publication">Publication:</label>
        <input
          id="publication"
          type="text"
          placeholder="Yes, No, etc."
          value={publication}
          onChange={(e) => setPublication(e.target.value)}
        />
      </div>

      <div className="filter-group">
        <label htmlFor="startDate">Start Date:</label>
        <input
          id="startDate"
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />
      </div>

      <div className="filter-group">
        <label htmlFor="endDate">End Date:</label>
        <input
          id="endDate"
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
        />
      </div>

      <div className="filter-actions">
        <button type="submit" className="btn-filter">Apply Filters</button>
        <button type="button" className="btn-reset" onClick={handleReset}>
          Reset
        </button>
      </div>
    </form>
  );
};

export default ExperimentFilter;