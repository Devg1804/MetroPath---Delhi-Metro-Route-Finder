-- Preloaded Delhi Metro Network data
SELECT * FROM stations;
INSERT INTO stations (name) VALUES
('Kashmere Gate'),
('Tis Hazari'),
('Shastri Park'),
('Inderlok'),
('Netaji Subhash Place'),
('Rajiv Chowk'),
('Karol Bagh'),
('Dwarka Sector 21'),
('Huda City Centre'),
('Chandni Chowk'),
('AIIMS'),
('Saket'),
('Pulbangash')
(Shaheed Sthal(First Station)
(Hindon River)
Arthala
Mohan Nagar
Shyam park
Major Mohit Sharma
Raj Bagh
Shaheed Nagar
Dilshad Garden
Jhil Mil
Mansarovar Park
Shahdara
Welcome [Conn: Pink]
Seelampur
Shastri Park
Kashmere Gate [Conn: Violet,Yellow]
Tis Hazari
Pul Bangash
Pratap Nagar
Shastri Nagar
Inderlok [Conn: Green]
Kanhaiya Nagar
Keshav Puram
Netaji Subash Place [Conn: Pink]
Kohat Enclave
Pitam Pura
Rohini East
Rohini West
Rithala(last station)


INSERT INTO lines (name) VALUES
('Red Line'),
('Blue Line'),
('Yellow Line');


-- Kashmere Gate is on both Red & Yellow Line
INSERT INTO station_lines (station_id, line_id) VALUES
-- (1, 1),  -- Kashmere Gate → Red Line
-- (1, 3),  -- Kashmere Gate → Yellow Line

-- (2, 1),  -- Tis Hazari → Red Line
-- (3, 1),  -- Shastri Park → Red Line
-- (4, 1),  -- Inderlok → Red Line
-- (5, 1),  -- Netaji Subhash Place → Red Line

-- (6, 2),  -- Rajiv Chowk → Blue Line
-- (6, 3),  -- Rajiv Chowk → Yellow Line (Interchange)

-- (7, 2),  -- Karol Bagh → Blue Line
-- (8, 2),  -- Dwarka Sector 21 → Blue Line

-- (9, 3),  -- Huda City Centre → Yellow Line
-- (10, 3), -- Chandni Chowk → Yellow Line
-- (11, 3), -- AIIMS → Yellow Line
-- (12, 3), -- Saket → Yellow Line
(14, 1); -- Pulbangash -> Red Line
SELECT * FROM stations WHERE name='Pulbangash';
INSERT INTO stations (id, name) VALUES (14, 'Pulbangash');
SELECT * FROM stations WHERE name IN ('Pulbangash', 'Kashmere Gate');


INSERT INTO routes (source_id, destination_id, distance) VALUES
-- (1, 2, 1.1),  -- Kashmere Gate to Tis Hazari
-- (2, 3, 2.3),  -- Tis Hazari to Shastri Park
-- (1, 4, 3.5),  -- Kashmere Gate to Inderlok
-- (4, 5, 2.1),  -- Inderlok to Netaji Subhash Place
-- (6, 7, 1.9),  -- Rajiv Chowk to Karol Bagh
-- (7, 8, 4.5),  -- Karol Bagh to Dwarka Sector 21
-- (9, 10, 3.0), -- Huda City Centre to Chandni Chowk
-- (10, 11, 2.7), -- Chandni Chowk to AIIMS
-- (11, 12, 3.1), -- AIIMS to Saket
(14, 2, 1.3);
-- (2, 14, 1.3);
SELECT * from routes

