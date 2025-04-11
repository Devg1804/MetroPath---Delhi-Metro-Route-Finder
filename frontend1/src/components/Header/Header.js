import React, { useState } from "react";
import { Link } from "react-router-dom";
import SearchBox from "../SearchBox/SearchBox"; // Import Search Box
import "./Header.css";
import logo from "../../assets/logo.png"; // Metro Logo

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Logo */}
        <Link to="/" className="logo">
          <img src={logo} alt="Delhi Metro" />
        </Link>

        \{/* Search Box */}
        <SearchBox />
        
        {/* Navigation Links */}
        <ul className={menuOpen ? "nav-links active" : "nav-links"}>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/metro-map">Metro Map</Link></li>
          <li><Link to="/route">Route</Link></li>
          <li><Link to="/fare">Fare</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>

        {/* Hamburger Menu for Mobile */}
        <div className="hamburger" onClick={() => setMenuOpen(!menuOpen)}>
          <div className={menuOpen ? "bar open" : "bar"}></div>
          <div className={menuOpen ? "bar open" : "bar"}></div>
          <div className={menuOpen ? "bar open" : "bar"}></div>
        </div>
      </div>
    </nav>
  );
};

export default Header;
