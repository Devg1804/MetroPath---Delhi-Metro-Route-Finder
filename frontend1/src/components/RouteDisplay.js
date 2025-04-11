import React from "react";
import MetroMap from "./MetroMap"; // Import the MetroMap component

const RouteDisplay = ({ routeData }) => {
  return (
    <div className="route-details">
      <h3>Route Details</h3>
      <p><strong>Shortest Path:</strong> {routeData.route.map(r => r.station).join(" → ")}</p>
      <p><strong>Total Distance:</strong> {routeData.total_distance} km</p>
      <p><strong>Fare:</strong> ₹{routeData.fare}</p>
      <p><strong>Estimated Time:</strong> {routeData.time} min</p>
      {routeData.interchanges > 0 && (
        <p><strong>Interchanges:</strong> {routeData.interchanges}</p>
      )}

      {/* Google Maps Button */}
      <button 
        onClick={() => window.open(`https://www.google.com/maps/dir/${routeData.route.map(r => encodeURIComponent(r.station)).join("/")}`, "_blank")}
        className="google-maps-button"
      >
        View on Google Maps
      </button>

      {/* Embed Interactive Google Map */}
      {routeData && <MetroMap routeData={routeData} />}
    </div>
  );
};

export default RouteDisplay;
