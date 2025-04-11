import React, { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import "./SearchBox.css";


const SearchBox = () => {
    const [query, setQuery] = useState("");
    const [suggestions, setSuggestions] = useState([]);
    const debounceTimeout = useRef(null);
    const navigate = useNavigate();
  
    // Function to fetch stations with a search query
    const fetchStations = async (searchTerm) => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/stations/${searchTerm}`);
        const data = await response.json();
  
        if (Array.isArray(data)) {
          setSuggestions(data);
        } else if (data.station) {
          // Convert API object into an array format
          setSuggestions([{ name: data.station, lines: data.lines }]);
        } else {
          setSuggestions([]);
        }
      } catch (error) {
        console.error("Error fetching stations:", error);
        setSuggestions([]);
      }
    };
  
    // Debounce the search input
    useEffect(() => {
      if (query.length > 1) {
        clearTimeout(debounceTimeout.current);
        debounceTimeout.current = setTimeout(() => {
          fetchStations(query);
        }, 300);
      } else {
        setSuggestions([]);
      }
  
      return () => clearTimeout(debounceTimeout.current);
    }, [query]);
  
    // Handle station selection
    const handleSelect = (station) => {
      setQuery(station.name);
      setSuggestions([]);
      navigate(`/stations/${encodeURIComponent(station.name)}`);
    };
  
    return (
      <div className="search-container">
        <input
          type="text"
          placeholder="Search Metro Station..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        {suggestions.length > 0 && (
          <ul className="suggestions">
            {suggestions.map((station) => (
              <li key={station.name} onClick={() => handleSelect(station)}>
                <strong>{station.name}</strong>
                <span> 🚇 {station.lines.join(", ")}</span>
              </li>
            ))}
          </ul>
        )}
      </div>
    );
  };
  
  export default SearchBox;

