SELECT Trip.place_from, COUNT(*)
FROM Trip
INNER JOIN Pass_in_trip ON Trip.id = Pass_in_trip.trip
INNER JOIN Passenger ON Passenger.id = Pass_in_trip.passenger
WHERE Passenger.name = 'Северус Снегг'
GROUP BY Trip.place_from;
