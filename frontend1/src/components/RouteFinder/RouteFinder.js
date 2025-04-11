import React, { useState, useEffect } from "react";
import { fetchStations, fetchShortestPath } from "../../api";
import "./RouteFinder.css";
// import GoogleMapComponent from "../GoogleMap"; // Import Google Map component
import GoogleMap from "../GoogleMap"; // Adjust path if needed

const RouteFinder = () => {
  const [stations, setStations] = useState([]);
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [routeData, setRouteData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [showMap, setShowMap] = useState(false);

  // Fetch all metro stations when component loads
  useEffect(() => {
    const getStations = async () => {
      try {
        const stationsList = await fetchStations();
        setStations(stationsList);
      } catch (err) {
        console.error("Error fetching stations:", err);
      }
    };
    getStations();
  }, []);

  // Handle route search
  const handleFindRoute = async () => {
    if (!source || !destination) {
      setError("Please select both source and destination.");
      return;
    }
    if (source === destination) {
      setError("Source and destination cannot be the same.");
      return;
    }
    setError("");
    setLoading(true);
    
    try {
      const route = await fetchShortestPath(source, destination);
      setRouteData(route);
    } catch (err) {
      console.error("Error fetching route:", err);
      setError("Failed to fetch route. Try again.");
    }
    
    setLoading(false);
  };

  return (
    <div className="route-finder">
      <h2>Find Metro Route</h2>
      <div className="dropdowns">
        <select value={source} onChange={(e) => setSource(e.target.value)}>
          <option value="">Select Source</option>
          {stations.map((station) => (
            <option key={station} value={station}>{station}</option>
          ))}
        </select>

        <select value={destination} onChange={(e) => setDestination(e.target.value)}>
          <option value="">Select Destination</option>
          {stations.map((station) => (
            <option key={station} value={station}>{station}</option>
          ))}
        </select>

        <button onClick={handleFindRoute} disabled={loading}>
          {loading ? "Finding Route..." : "Find Route"}
        </button>
      </div>

      {error && <p className="error">{error}</p>}

      {routeData && (
        <div className="route-details">
            <h3>Route Details</h3>
            <p><strong>Shortest Path:</strong> {routeData.route.map(r => r.station).join(" → ")}</p>
            <p><strong>Total Distance:</strong> {routeData.total_distance} km</p>
            <p><strong>Fare:</strong> ₹{routeData.fare}</p>
            {/* <p><strong>Estimated Time:</strong> {routeData.time} min</p> */}
            {routeData.interchanges > 0 && (
            <p><strong>Interchanges:</strong> {routeData.interchanges}</p>
            )}
            {/* 🚀 View on Map Button */}
            <button onClick={() => setShowMap(!showMap)}>
                {showMap ? "Hide Map" : "View on Map"}
            </button>

            {/* 🔥 Render Google Map when button is clicked */}
            <GoogleMap source={routeData.route[0].station} destination={routeData.route[routeData.route.length - 1].station} />
            {/* {showMap && (
            <GoogleMapComponent
              source={routeData.route[0].station} // First station
              destination={routeData.route[routeData.route.length - 1].station} // Last station
            /> */}
            
        </div>
        )}
    </div>
  );
};

export default RouteFinder;
