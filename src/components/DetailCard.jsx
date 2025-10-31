import React from 'react';

const DetailCard = ({ movie, onClose, isFavorite, toggleFavorite }) => {
  return (
    <>
      <div className="modal-overlay" onClick={onClose}></div>
      <div className="modal">
        <h2>{movie.Title}</h2>
        <img src={movie.Poster !== 'N/A' ? movie.Poster : 'placeholder.jpg'} alt={movie.Title} />
        <p><strong>Year:</strong> {movie.Year}</p>
        <p><strong>Rated:</strong> {movie.Rated}</p>
        <p><strong>Released:</strong> {movie.Released}</p>
        <p><strong>Runtime:</strong> {movie.Runtime}</p>
        <p><strong>Genre:</strong> {movie.Genre}</p>
        <p><strong>Director:</strong> {movie.Director}</p>
        <p><strong>Actors:</strong> {movie.Actors}</p>
        <p><strong>Plot:</strong> {movie.Plot}</p>
        <p><strong>IMDB Rating:</strong> {movie.imdbRating}</p>
        <button onClick={onClose}>Close</button>
        <button
          className="favorite-btn"
          onClick={toggleFavorite}
        >
          {isFavorite ? 'Remove from Favorites' : 'Add to Favorites'}
        </button>
      </div>
    </>
  );
};

export default DetailCard;