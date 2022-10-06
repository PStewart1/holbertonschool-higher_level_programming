-- lists all cities contained in the database hbtn_0d_usa
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name 
    FROM cities 
    LEFT JOIN states 
    ON state_id = states.id
    ORDER BY cities.id ASC