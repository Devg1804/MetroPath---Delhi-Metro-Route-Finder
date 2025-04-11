import secrets
print(secrets.token_hex(32))  # Generates a 64-character secure key
from app.services.shortest_path import MetroGraph
metro = MetroGraph()
print(metro.get_station_id("Pulbangash"))  # Should print 14
print(metro.get_station_id("Tis Hazari"))
print(metro.graph.nodes(data=True))
# python -m app.main
