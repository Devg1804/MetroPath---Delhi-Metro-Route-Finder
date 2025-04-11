// import React from "react";
// import { GoogleMap, LoadScript, DirectionsService, DirectionsRenderer } from "@react-google-maps/api";

// const containerStyle = {
//   width: "100%",
//   height: "400px",
// };

// const center = {
//   lat: 28.6139, // Default to New Delhi
//   lng: 77.2090,
// };

// const GoogleMapComponent = ({ source, destination }) => {
//   const [directions, setDirections] = React.useState(null);

//   React.useEffect(() => {
//     if (source && destination) {
//       const directionsService = new window.google.maps.DirectionsService();
//       directionsService.route(
//         {
//           origin: source,
//           destination: destination,
//           travelMode: window.google.maps.TravelMode.TRANSIT, // Metro uses public transit
//         },
//         (result, status) => {
//           if (status === window.google.maps.DirectionsStatus.OK) {
//             setDirections(result);
//           } else {
//             console.error(`Error fetching directions: ${status}`);
//           }
//         }
//       );
//     }
//   }, [source, destination]);

//   return (
//     <LoadScript googleMapsApiKey="AIzaSyBngx4z0xwnaDNYgNeGb_1eipSNW1RUE1k">
//       <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={12}>
//         {directions && <DirectionsRenderer directions={directions} />}
//       </GoogleMap>
//     </LoadScript>
//   );
// };

// export default GoogleMapComponent;
import { useEffect, useState } from "react";

const GoogleMap = ({ source, destination }) => {
  const [directions, setDirections] = useState(null);

  useEffect(() => {
    if (!window.google) return;

    const directionsService = new window.google.maps.DirectionsService();
    
    directionsService.route(
      {
        origin: source,
        destination: destination,
        travelMode: window.google.maps.TravelMode.TRANSIT, // Use TRANSIT for metro
      },
      (result, status) => {
        if (status === "OK") {
          setDirections(result);
        } else {
          console.error("Error fetching directions:", status);
        }
      }
    );
  }, [source, destination]);

  return (
    <div>
      {directions ? (
        <div>
          <h3>Route Details</h3>
          <p><strong>Distance:</strong> {directions.routes[0].legs[0].distance.text}</p>
          <p><strong>Estimated Time:</strong> {directions.routes[0].legs[0].duration.text}</p>
        </div>
      ) : (
        <p>Loading directions...</p>
      )}
    </div>
  );
};

export default GoogleMap;
