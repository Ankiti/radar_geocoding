# radar_geocoding

A python program to check if there is a geofence nearby using Radar API. 
I have set up two geofences: 
1. University of Waterloo -> Center: (43.473027156660876, -80.54154600510986); Radius: 381 meters
2. University of Toronto -> Center: (43.66290564970717, -79.39602309575469); Radius: 100 meters

The program asks the user to enter a location, changes that location to coordinates using Forward Geocoding in Radar. 
Then, it checks if there is a geofence near that location using Geofences search in Radar and returns the description of the geofence if there is one.
