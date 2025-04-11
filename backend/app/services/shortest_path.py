# import networkx as nx
# from app.utils.db import get_db_connection

# class MetroGraph:
#     def __init__(self):
#         """Initialize the metro graph with stations, routes, and lines."""
#         self.graph = nx.Graph()  # Undirected graph for metro routes
#         self.station_lines = {}   # Map stations to metro lines
#         self.load_data()

#     def load_data(self):
#         """Load stations, routes, and line information from the database."""
#         conn = get_db_connection()
#         cur = conn.cursor()

#         # Load stations and their lines
#         cur.execute("""
#             SELECT s.id, s.name, l.name 
#             FROM stations s
#             JOIN station_lines sl ON s.id = sl.station_id
#             JOIN lines l ON sl.line_id = l.id
#         """)
#         for station_id, station_name, line_name in cur.fetchall():
#             self.graph.add_node(station_id, name=station_name)
#             if station_name not in self.station_lines:
#                 self.station_lines[station_name] = []
#             self.station_lines[station_name].append(line_name)

#         # Load routes (edges with distances)
#         cur.execute("SELECT source_id, destination_id, distance FROM routes")
#         for src, dest, distance in cur.fetchall():
#             self.graph.add_edge(src, dest, weight=distance)

#         cur.close()
#         conn.close()

#     def find_shortest_path(self, source, destination):
#         """Find the shortest path considering minimum interchanges."""
#         if source not in self.station_lines or destination not in self.station_lines:
#             return {"error": "Invalid station name."}

#         # Convert station names to IDs
#         source_id = self.get_station_id(source)
#         destination_id = self.get_station_id(destination)

#         # Find shortest path using Dijkstra
#         path = nx.shortest_path(self.graph, source=source_id, target=destination_id, weight="weight")
        
#         # Convert station IDs back to names
#         station_path = [self.get_station_name(station_id) for station_id in path]

#         # Count interchanges
#         interchanges = self.calculate_interchanges(station_path)

#         return {
#             "route": station_path,
#             "total_distance": self.calculate_distance(path),
#             "interchanges": interchanges
#         }

#     def get_station_id(self, station_name):
#         """Get station ID from name."""
#         for station_id, data in self.graph.nodes(data=True):
#             if data["name"] == station_name:
#                 return station_id
#         return None

#     def get_station_name(self, station_id):
#         """Get station name from ID."""
#         return self.graph.nodes[station_id]["name"]

#     def calculate_distance(self, path):
#         """Calculate total distance of the path."""
#         distance = 0
#         for i in range(len(path) - 1):
#             distance += self.graph[path[i]][path[i + 1]]["weight"]
#         return round(distance, 2)

#     def calculate_interchanges(self, station_path):
#         """Calculate number of interchanges in a given route."""
#         prev_line = None
#         interchanges = 0
#         for station in station_path:
#             available_lines = self.station_lines.get(station, [])
#             if prev_line and prev_line not in available_lines:
#                 interchanges += 1
#             prev_line = available_lines[0] if available_lines else None
#         return interchanges


# import networkx as nx
# from app.utils.db import get_db_connection
# from collections import deque

# class MetroGraph:
#     def __init__(self):
#         """Initialize the metro graph with stations, routes, and lines."""
#         self.graph = nx.Graph()  # Undirected graph for metro routes
#         self.station_lines = {}   # Map stations to metro lines
#         self.load_data()

#     def load_data(self):
#         """Load stations, routes, and line information from the database."""
#         conn = get_db_connection()
#         cur = conn.cursor()

#         # Load stations and their lines
#         cur.execute("""
#             SELECT s.id, s.name, l.name 
#             FROM stations s
#             JOIN station_lines sl ON s.id = sl.station_id
#             JOIN lines l ON sl.line_id = l.id
#         """)
#         for station_id, station_name, line_name in cur.fetchall():
#             self.graph.add_node(station_id, name=station_name)
#             if station_name not in self.station_lines:
#                 self.station_lines[station_name] = []
#             self.station_lines[station_name].append(line_name)

#         # Load routes (edges with distances)
#         cur.execute("SELECT source_id, destination_id, distance FROM routes")
#         for src, dest, distance in cur.fetchall():
#             self.graph.add_edge(src, dest, weight=distance)

#         cur.close()
#         conn.close()

#     def find_shortest_path(self, source, destination, method="dijkstra"):
#         """Find the shortest path using Dijkstra or BFS.
        
#         - method="dijkstra" -> Uses Dijkstra's algorithm (shortest distance)
#         - method="bfs" -> Uses BFS (minimum interchanges)
#         """
#         if source not in self.station_lines or destination not in self.station_lines:
#             return {"error": "Invalid station name."}

#         # Convert station names to IDs
#         source_id = self.get_station_id(source)
#         destination_id = self.get_station_id(destination)

#         if method == "bfs":
#             path = self.find_bfs_path(source_id, destination_id)  # BFS for min interchanges
#         else:
#             path = nx.shortest_path(self.graph, source=source_id, target=destination_id, weight="weight")  # Dijkstra

#         # Convert station IDs back to names
#         station_path = [self.get_station_name(station_id) for station_id in path]

#         return {
#             "route": station_path,
#             "total_distance": self.calculate_distance(path),
#             "interchanges": self.calculate_interchanges(station_path)
#         }

#     def find_bfs_path(self, source_id, destination_id):
#         """Finds the path with the **minimum interchanges** using BFS."""
#         queue = deque([(source_id, [])])  # (Current station, path taken)
#         visited = set()

#         while queue:
#             station, path = queue.popleft()
#             path = path + [station]

#             if station == destination_id:
#                 return path  # Found shortest path with least interchanges

#             if station not in visited:
#                 visited.add(station)
#                 for neighbor in self.graph.neighbors(station):
#                     queue.append((neighbor, path))

#         return []  # No path found

#     def get_station_id(self, station_name):
#         """Get station ID from name."""
#         for station_id, data in self.graph.nodes(data=True):
#             if data["name"] == station_name:
#                 return station_id
#         return None

#     def get_station_name(self, station_id):
#         """Get station name from ID."""
#         return self.graph.nodes[station_id]["name"]

#     def calculate_distance(self, path):
#         """Calculate total distance of the path."""
#         distance = 0
#         for i in range(len(path) - 1):
#             distance += self.graph[path[i]][path[i + 1]]["weight"]
#         return round(distance, 2)

#     def calculate_interchanges(self, station_path):
#         """Calculate number of interchanges in a given route."""
#         prev_line = None
#         interchanges = 0
#         for station in station_path:
#             available_lines = self.station_lines.get(station, [])
#             if prev_line and prev_line not in available_lines:
#                 interchanges += 1
#             prev_line = available_lines[0] if available_lines else None
#         return interchanges
import heapq
from collections import defaultdict
from app.utils.db import get_db_connection

class MetroGraph:
    def __init__(self):
        """Initialize the metro graph from database."""
        self.graph = defaultdict(list)  # Adjacency list representation
        self.station_names = {}  # Maps station ID to name
        self.station_ids = {}  # Maps station name to ID
        self.station_lines = {}  # Maps station name to metro lines
        self.load_data()

    def load_data(self):
        """Load stations and routes from the database."""
        conn = get_db_connection()
        cur = conn.cursor()

        # Load stations
        cur.execute("SELECT id, name FROM stations")
        for station_id, station_name in cur.fetchall():
            self.station_names[station_id] = station_name
            self.station_ids[station_name] = station_id
            self.station_lines[station_name] = []

        # Load station-line mappings
        cur.execute("""
            SELECT s.name, l.name 
            FROM stations s
            JOIN station_lines sl ON s.id = sl.station_id
            JOIN lines l ON sl.line_id = l.id
        """)
        for station_name, line_name in cur.fetchall():
            self.station_lines[station_name].append(line_name)

        # Load routes (edges with distances)
        cur.execute("SELECT source_id, destination_id, distance FROM routes")
        for src, dest, distance in cur.fetchall():
            self.graph[src].append((dest, distance))
            self.graph[dest].append((src, distance))  # Undirected graph

        cur.close()
        conn.close()

    def find_shortest_path(self, source, destination, method="dijkstra"):
        """Find shortest path using Dijkstra or BFS"""
        if source not in self.station_ids or destination not in self.station_ids:
            return {"error": "Invalid station name."}

        source_id = self.station_ids[source]
        destination_id = self.station_ids[destination]

        if method == "bfs":
            path = self.find_bfs_path(source_id, destination_id)
        else:
            path = self.dijkstra(source_id, destination_id)

        if not path:
            return {"error": "No path found."}

        station_path = [self.station_names[station_id] for station_id in path]

        return {
            "route": station_path,
            "total_distance": self.calculate_distance(path),
            "interchanges": self.calculate_interchanges(station_path)
        }

    def dijkstra(self, source_id, destination_id):
        """Manual Dijkstra's algorithm for shortest distance"""
        priority_queue = [(0, source_id, [])]  # (cost, station_id, path)
        visited = {}

        while priority_queue:
            cost, station, path = heapq.heappop(priority_queue)

            if station in visited and visited[station] <= cost:
                continue
            visited[station] = cost

            path = path + [station]

            if station == destination_id:
                return path  # Found shortest path

            for neighbor, weight in self.graph[station]:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

        return []

    def find_bfs_path(self, source_id, destination_id):
        """Find shortest path with minimum interchanges using BFS"""
        from collections import deque
        queue = deque([(source_id, [])])
        visited = set()

        while queue:
            station, path = queue.popleft()
            path = path + [station]

            if station == destination_id:
                return path

            if station not in visited:
                visited.add(station)
                for neighbor, _ in self.graph[station]:
                    queue.append((neighbor, path))

        return []

    def calculate_distance(self, path):
        """Calculate total travel distance"""
        distance = 0
        for i in range(len(path) - 1):
            for neighbor, weight in self.graph[path[i]]:
                if neighbor == path[i + 1]:
                    distance += weight
                    break
        return round(distance, 2)

    def calculate_interchanges(self, station_path):
        """Calculate interchanges"""
        prev_line = None
        interchanges = 0

        for station in station_path:
            available_lines = self.station_lines.get(station, [])
            if prev_line and prev_line not in available_lines:
                interchanges += 1
            prev_line = available_lines[0] if available_lines else None

        return interchanges
    def get_station_id(self, station_name):
        """Get station ID from station name."""
        return self.station_ids.get(station_name, None)

    def get_station_name(self, station_id):
        """Get station name from station ID."""
        return self.station_names.get(station_id, None)
