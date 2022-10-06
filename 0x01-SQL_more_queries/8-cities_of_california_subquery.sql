--  lists all the cities of California that can be found in the database hbtn_0d_usa
--  he database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name FROM cities, states WHERE states.name = 'California' AND state_id = states.id ORDER BY cities.id