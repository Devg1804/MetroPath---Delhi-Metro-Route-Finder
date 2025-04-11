import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; // Change this if your backend runs on a different port

// Get all metro stations
export const fetchStations = async () => {
    const response = await axios.get(`${API_BASE_URL}/stations/`);
    return response.data.stations;
};

// Get station details
export const fetchStationDetails = async (station) => {
    const response = await axios.get(`${API_BASE_URL}/stations/${encodeURIComponent(station)}`);
    return response.data;
};

// Get shortest path
export const fetchShortestPath = async (source, destination) => {
    const response = await axios.get(`${API_BASE_URL}/metro/shortest-path`, {
        params: { source, destination }
    });
    return response.data;
};
