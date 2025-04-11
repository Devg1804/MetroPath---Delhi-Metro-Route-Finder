import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const StationDetails = () => {
  const { name } = useParams(); // Get station name from URL
  const [station, setStation] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStationDetails = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/stations/${encodeURIComponent(name)}`);
        const data = await response.json();
        setStation(data);
      } catch (error) {
        console.error("Error fetching station details:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchStationDetails();
  }, [name]);

  if (loading) return <p>Loading...</p>;
  if (!station) return <p>No station found</p>;

  return (
    <div className="station-details">
      <h2>🚇 {station.station}</h2>
      <p><strong>Lines:</strong> {station.lines.join(", ")}</p>
      <p><strong>Nearby Places:</strong> {station.nearby_places.join(", ")}</p>
    </div>
  );
};

export default StationDetails;

