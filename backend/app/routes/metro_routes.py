from flask import Blueprint, request, jsonify
from app.services.shortest_path import MetroGraph
from app.services.fare_calculator import FareCalculator
from app.utils.db import get_db_connection

metro_routes_bp = Blueprint("metro_routes", __name__, url_prefix="/metro")

# Initialize metro graph
metro_graph = MetroGraph()

def get_station_lines(station_name):
    """
    Fetch the metro lines a station belongs to.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    query = """
    SELECT l.name FROM lines l
    JOIN station_lines sl ON l.id = sl.line_id
    JOIN stations s ON s.id = sl.station_id
    WHERE s.name = %s;
    """
    cur.execute(query, (station_name,))
    lines = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    
    return lines

@metro_routes_bp.route("/shortest-path", methods=["GET"])
def get_shortest_path():
    """
    API Endpoint: Get the shortest path and fare between two stations, including metro line info.
    Example Request: /metro/shortest-path?source=Rajiv Chowk&destination=Noida City Centre
    """
    source = request.args.get("source")
    destination = request.args.get("destination")

    if not source or not destination:
        return jsonify({"error": "Source and destination are required."}), 400

    # Find shortest path
    result = metro_graph.find_shortest_path(source, destination)

    if "error" in result:
        return jsonify(result), 400

    # Get lines for each station
    route_with_lines = [
        {"station": station, "lines": get_station_lines(station)}
        for station in result["route"]
    ]

    # Calculate fare
    fare = FareCalculator.calculate_fare(result["total_distance"], result["interchanges"])

    # Final response
    response = {
        "route": route_with_lines,
        "total_distance": result["total_distance"],
        "interchanges": result["interchanges"],
        "fare": fare
    }

    return jsonify(response), 200
