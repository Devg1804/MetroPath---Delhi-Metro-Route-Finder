class FareCalculator:
    @staticmethod
    def calculate_fare(distance, interchanges):
        """
        Calculate fare based on distance and number of interchanges.
        """
        # Base fare slabs
        if distance <= 2:
            fare = 10
        elif distance <= 5:
            fare = 20
        elif distance <= 10:
            fare = 30
        elif distance <= 20:
            fare = 40
        else:
            fare = 50  # Max fare for distances > 20 km

        # Additional cost for interchanges
        fare += interchanges * 5  # ₹5 per interchange

        return fare
