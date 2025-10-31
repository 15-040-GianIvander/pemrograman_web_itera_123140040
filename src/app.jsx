import React, { useState, useEffect } from 'react';
import './App.css';
import Header from './components/Header';
import SearchForm from './components/SearchForm';
import DataTable from './components/DataTable';
import DetailCard from './components/DetailCard';

const API_KEY = 'd480045c';
const API_BASE = 'http://www.omdbapi.com/';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [year, setYear] = useState('');
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [favorites, setFavorites] = useState([]);
  const [showFavorites, setShowFavorites] = useState(false);

  useEffect(() => {
    const storedFavorites = JSON.parse(localStorage.getItem('favorites')) || [];
    setFavorites(storedFavorites);
  }, []);

  useEffect(() => {
    localStorage.setItem('favorites', JSON.stringify(favorites));
  }, [favorites]);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!searchTerm) return;

    const url = `${API_BASE}?s=${encodeURIComponent(searchTerm)}&y=${year}&apikey=${API_KEY}&type=movie`;
    const response = await fetch(url);
    const data = await response.json();
    if (data.Response === 'True') {
      setMovies(data.Search);
      setShowFavorites(false);
    } else {
      setMovies([]);
    }
  };

  const fetchMovieDetails = async (imdbID) => {
    const url = `${API_BASE}?i=${imdbID}&apikey=${API_KEY}`;
    const response = await fetch(url);
    const data = await response.json();
    setSelectedMovie(data);
  };

  const toggleFavorite = (movie) => {
    const isFavorite = favorites.some((fav) => fav.imdbID === movie.imdbID);
    if (isFavorite) {
      setFavorites(favorites.filter((fav) => fav.imdbID !== movie.imdbID));
    } else {
      setFavorites([...favorites, movie]);
    }
  };

  const showFavoritesList = () => {
    setMovies(favorites);
    setShowFavorites(true);
    setSelectedMovie(null);
  };

  return (
    <div className="App">
      <Header onShowFavorites={showFavoritesList} />
      <SearchForm
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        year={year}
        setYear={setYear}
        handleSearch={handleSearch}
      />
      <DataTable
        movies={movies}
        fetchMovieDetails={fetchMovieDetails}
        favorites={favorites}
        toggleFavorite={toggleFavorite}
        isFavorites={showFavorites}
      />
      {selectedMovie && (
        <DetailCard
          movie={selectedMovie}
          onClose={() => setSelectedMovie(null)}
          isFavorite={favorites.some((fav) => fav.imdbID === selectedMovie.imdbID)}
          toggleFavorite={() => toggleFavorite(selectedMovie)}
        />
      )}
    </div>
  );
}

export default App;