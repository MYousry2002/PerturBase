// src/pages/Experiment.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';
import './Experiment.css'; // Update the CSS file name accordingly

const Experiment = () => {
  const { expId } = useParams();  // Assuming the route is like /experiments/:expId
  const [experiment, setExperiment] = useState(null);
  const [channels, setChannels] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch experiment details
    api.get(`/experiments/${expId}`)
      .then(response => {
        setExperiment(response.data);
      })
      .catch(err => {
        setError(err);
      });

    // Fetch related channel metadata
    api.get(`/channels/experiment/${expId}`)
      .then(response => {
        setChannels(response.data);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, [expId]);

  if (loading) return <p>Loading experiment details...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div className="experiment-container">
      {experiment ? (
        <>
          <h1>{experiment.Name}</h1>
          <p><strong>Date:</strong> {experiment.Date}</p>
          <p><strong>Treatment:</strong> {experiment.Treatment}</p>
          <p><strong>Source:</strong> {experiment.Source}</p>
          <p><strong>Publication:</strong> {experiment.Publication}</p>
          
          <h2>Channel Details</h2>
          {channels.length > 0 ? (
            <table className="channel-table">
              <thead>
                <tr>
                  <th>CMID</th>
                  <th>Type</th>
                  <th>Ncells</th>
                  <th>Nfeatures_avg</th>
                  <th>Ncount_avg</th>
                  <th>Mito_avg</th>
                  <th>Ribo_avg</th>
                </tr>
              </thead>
              <tbody>
                {channels.map(channel => (
                  <tr key={channel.CMID}>
                    <td>{channel.CMID}</td>
                    <td>{channel.Type}</td>
                    <td>{channel.Ncells}</td>
                    <td>{channel.Nfeatures_avg}</td>
                    <td>{channel.Ncount_avg}</td>
                    <td>{channel.Mito_avg}</td>
                    <td>{channel.Ribo_avg}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No channel data available.</p>
          )}
        </>
      ) : (
        <p>Experiment not found.</p>
      )}
    </div>
  );
};

export default Experiment;