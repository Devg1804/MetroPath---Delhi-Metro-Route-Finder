from flask import Flask
from app.routes.stations import stations_bp
from app.routes.metro_routes import metro_routes_bp
from app.utils.db import get_db_connection
from flask_cors import CORS
app = Flask(__name__)

CORS(app)  # Allow frontend requests
# Register API routes
app.register_blueprint(stations_bp, url_prefix="/stations")
app.register_blueprint(metro_routes_bp, url_prefix="/metro")

@app.route("/")
def home():
    return "Delhi Metro API is running!"

# Initialize Database (if needed)
get_db_connection()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
