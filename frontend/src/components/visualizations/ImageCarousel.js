//  src/components/visualizations/ImageCarousel.js

import React, { useState } from 'react';
import './ImageCarousel.css';

const ImageCarousel = ({ imageUrls }) => {
  const [index, setIndex] = useState(0);
  const validImages = Array.isArray(imageUrls) ? imageUrls.filter(Boolean) : [];

  const handlePrev = () => {
    setIndex((prev) => (prev - 1 + validImages.length) % validImages.length);
  };

  const handleNext = () => {
    setIndex((prev) => (prev + 1) % validImages.length);
  };

  if (validImages.length === 0) {
    return <div className="carousel-placeholder">No images available.</div>;
  }

  return (
    <div className="carousel-container">
      <div className="carousel-content">
        <button onClick={handlePrev} className="carousel-nav left">&lt;</button>
        <div className="carousel-image-wrapper">
          <img
            src={validImages[index]}
            alt={`Slide ${index + 1}`}
            onError={(e) => {
              e.target.onerror = null;
              e.target.src = '/plots/fallback.png';
            }}
          />
        </div>
        <button onClick={handleNext} className="carousel-nav right">&gt;</button>
      </div>
      <div className="carousel-dots">
        {validImages.map((_, i) => (
          <span
            key={i}
            className={`carousel-dot ${i === index ? 'active' : ''}`}
            onClick={() => setIndex(i)}
          />
        ))}
      </div>
    </div>
  );
};

export default ImageCarousel;