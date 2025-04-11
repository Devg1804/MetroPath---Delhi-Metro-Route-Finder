-- schema for station and routes
-- stations table(only stations name)
CREATE TABLE stations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- lines table
CREATE TABLE lines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- station_lines Table 
-- If a station belongs to multiple lines, it will have multiple entries in station_lines.
CREATE TABLE station_lines (
    station_id INTEGER NOT NULL REFERENCES stations(id) ON DELETE CASCADE,
    line_id INTEGER NOT NULL REFERENCES lines(id)ON DELETE CASCADE,
    PRIMARY KEY (station_id, line_id)
);

-- Routes Table - Stores distance between stations.
CREATE TABLE routes (
    source_id INTEGER NOT NULL REFERENCES stations(id) ON DELETE CASCADE,
    destination_id INTEGER NOT NULL REFERENCES stations(id) ON DELETE CASCADE,
    distance DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (source_id, destination_id)
)


CREATE DATABASE metro_db;
\c metro_db;
