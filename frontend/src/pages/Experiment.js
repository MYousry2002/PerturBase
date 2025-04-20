// src/pages/Experiment.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';
import ImageCarousel from '../components/visualizations/ImageCarousel';
import './Experiment.css';

const Experiment = () => {
  const { expId } = useParams();
  const [experiment, setExperiment] = useState(null);
  const [channels, setChannels] = useState([]);
  const [activeTab, setActiveTab] = useState('Visualization');
  const [activeView, setActiveView] = useState('Metrics');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    api.get(`/api/experiments/${expId}`)
      .then(res => setExperiment(res.data))
      .catch(err => setError(err));

    api.get(`/api/channels/experiment/${expId}`)
      .then(res => {
        setChannels(res.data);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, [expId]);

  if (loading || !experiment) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  const normalizeView = (view) => view.toLowerCase().replace(/\s+/g, '_');

  const PlotSection = ({ expId, view }) => {
    const [plotImages, setPlotImages] = useState([]);

    useEffect(() => {
      const normalized = normalizeView(view);
      api.get(`/api/plots/${expId}/${normalized}`)
        .then(res => {
          setPlotImages(res.data);
        })
        .catch(err => {
          setPlotImages([]);
        });
    }, [expId, view]);

    return plotImages.length > 0 ? (
      <ImageCarousel imageUrls={plotImages} />
    ) : (
      <p>No plots available for this view.</p>
    );
  };

  return (
    <div className="experiment-page">
      <h1 className="experiment-title">{experiment.Name}</h1>

      <div className="experiment-tabs">
        {['Metadata', 'Visualization', 'Download'].map(tab => (
          <button
            key={tab}
            className={tab === activeTab ? 'active' : ''}
            onClick={() => setActiveTab(tab)}
          >
            {tab}
          </button>
        ))}
      </div>

      {activeTab === 'Metadata' && (
        <div className="metadata-section">
          <p><strong>Date:</strong> {experiment.Date}</p>
          <p><strong>Treatment:</strong> {experiment.Treatment}</p>
          <p><strong>Source:</strong> {experiment.Source}</p>
          <p><strong>Publication:</strong> {experiment.Publication}</p>
          <h2>Channel Details</h2>
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
              {channels.map(c => (
                <tr key={c.CMID}>
                  <td>{c.CMID}</td>
                  <td>{c.Type}</td>
                  <td>{c.Ncells}</td>
                  <td>{c.Nfeatures_avg}</td>
                  <td>{c.Ncount_avg}</td>
                  <td>{c.Mito_avg}</td>
                  <td>{c.Ribo_avg}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {activeTab === 'Visualization' && (
        <div className="visualization-section">
          <aside className="left-sidebar">
            {['Metrics', 'Umap', 'Top Genes', 'Heatmap'].map(view => (
              <button
                key={view}
                className={activeView === view ? 'active' : ''}
                onClick={() => setActiveView(view)}
              >
                {view}
              </button>
            ))}
          </aside>
          <main className="visualization-content">
            <PlotSection expId={expId} view={activeView} />
          </main>
        </div>
      )}

      {activeTab === 'Download' && (
        <div className="download-section">
          <p>Raw data files can be downloaded below:</p>
          <a href={`/api/downloads/experiment/${expId}`} className="btn-download">
            Download Raw Files
          </a>
        </div>
      )}
    </div>
  );
};

export default Experiment;