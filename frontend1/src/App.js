import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header/Header";
import StationDetails from "./pages/StationDetails";
import RouteFinder from "./components/RouteFinder/RouteFinder";

const App = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<h1>Home Page</h1>} />
        <Route path="/metro-map" element={<h1>Metro Map</h1>} />
        <Route path="/route" element={<RouteFinder />} />
        <Route path="/fare" element={<h1>Fare Details</h1>} />
        <Route path="/contact" element={<h1>Contact Us</h1>} />
        <Route path="/stations/:name" element={<StationDetails />} />
      </Routes>
    </Router>
  );
};

export default App;
