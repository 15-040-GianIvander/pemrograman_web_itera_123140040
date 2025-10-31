import React from 'react';

const DataTable = ({ movies, fetchMovieDetails, favorites, toggleFavorite, isFavorites }) => {
  return (
    <div className="movie-grid">
      {movies.map((movie) => (
        <div key={movie.imdbID} className="movie-card">
          <img src={movie.Poster !== 'N/A' ? movie.Poster : 'placeholder.jpg'} alt={movie.Title} />
          <div className="movie-info">
            <h3>{movie.Title}</h3>
            <p>Year: {movie.Year}</p>
            <p>Rating: {movie.imdbRating || 'N/A'}</p>
            <button onClick={() => fetchMovieDetails(movie.imdbID)}>Details</button>
            <button
              className="favorite-btn"
              onClick={() => toggleFavorite(movie)}
            >
              {favorites.some((fav) => fav.imdbID === movie.imdbID) ? 'Remove Favorite' : 'Add Favorite'}
            </button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default DataTable;