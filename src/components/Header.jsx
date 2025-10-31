import React from 'react';

const Header = ({ onShowFavorites }) => {
  return (
    <header>
      <h1>Movie Database Explorer</h1>
      <button onClick={onShowFavorites}>Show Favorites</button>
    </header>
  );
};

export default Header;