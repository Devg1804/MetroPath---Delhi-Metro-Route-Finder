from flask import Blueprint, request, jsonify
from app.utils.db import get_db_connection

stations_bp = Blueprint("stations", __name__, url_prefix="/stations")

@stations_bp.route("/", methods=["GET"])
def get_all_stations():
    """
    API Endpoint: Get a list of all metro stations.
    Example Request: /stations/
    """
    conn = get_db_connection()
    cur = conn.cursor()

    query = "SELECT name FROM stations ORDER BY name;"
    cur.execute(query)
    stations = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()

    return jsonify({"stations": stations}), 200


@stations_bp.route("/<station_name>", methods=["GET"])
def get_station_details(station_name):
    """
    API Endpoint: Get details of a specific station (Lines, Nearby Places, etc.).
    Example Request: /stations/Rajiv%20Chowk
    """
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch station details (lines)
    query = """
    SELECT l.name FROM lines l
    JOIN station_lines sl ON l.id = sl.line_id
    JOIN stations s ON s.id = sl.station_id
    WHERE s.name = %s;
    """
    cur.execute(query, (station_name,))
    lines = [row[0] for row in cur.fetchall()]

    if not lines:
        return jsonify({"error": "Station not found"}), 404

    # Fetch nearby places (optional: you can extend this with more data)
    nearby_places = {
        "Rajiv Chowk": ["Connaught Place", "Palika Bazaar"],
        "Noida City Centre": ["GIP Mall", "Atta Market"],
        "Mandi House": ["National School of Drama", "Agrasen ki Baoli"],
        "Kashmere Gate": ["Tis Hazari"]
    }

    response = {
        "station": station_name,
        "lines": lines,
        "nearby_places": nearby_places.get(station_name, [])
    }

    cur.close()
    conn.close()

    return jsonify(response), 200
