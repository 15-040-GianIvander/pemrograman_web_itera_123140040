import React from 'react';

const SearchForm = ({ searchTerm, setSearchTerm, year, setYear, handleSearch }) => {
  return (
    <form onSubmit={handleSearch}>
      <input
        type="text"
        placeholder="Search for a movie..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <input
        type="number"
        placeholder="Year (optional)"
        value={year}
        onChange={(e) => setYear(e.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  );
};

export default SearchForm;