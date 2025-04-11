import { GoogleMap, LoadScript, Marker, Polyline } from "@react-google-maps/api";

const MetroMap = ({ routeData }) => {
  const mapCenter = { lat: 28.6139, lng: 77.2090 }; // Default to Delhi

  return (
    <LoadScript googleMapsApiKey="AIzaSyBngx4z0xwnaDNYgNeGb_1eipSNW1RUE1k">
      <GoogleMap 
        mapContainerStyle={{ width: "100%", height: "400px" }} 
        center={mapCenter} 
        zoom={12}
      >
        {routeData.route.map((r, index) => (
          <Marker key={index} position={{ lat: r.lat, lng: r.lng }} label={r.station} />
        ))}

        {/* Draw route line */}
        <Polyline 
          path={routeData.route.map(r => ({ lat: r.lat, lng: r.lng }))} 
          options={{ strokeColor: "#ff0000", strokeWeight: 4 }}
        />
      </GoogleMap>
    </LoadScript>
  );
};

export default MetroMap;
