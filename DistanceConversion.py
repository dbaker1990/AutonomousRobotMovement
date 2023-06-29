from haversine import haversine, Unit
import utm
import math
import numpy as np
import sys


#Get the distance of two points in meters
def DistanceBetweenTwoPoints(lat1: float, lon1: float, lat2: float, lon2: float):
    
    point1 = (lat1,lon1)
    point2 = (lat2,lon1)
    
    return haversine(point1,point2, unit='m')

#convert longtitude and latitude to x,y,z coordinates
def ConvertToXYZ(lat: float, lon:float):
    R = 6371
    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    z = R * np.sin(lat)
    print(x, y, z)
    return x,y,z

#convert XYZ to Latitude and Longitude
def XYZToLongLat(x:float, y: float, z: float):
    R = 6371
    lat = np.degrees(np.arcsin(z/R))
    lon = np.degrees(np.arctan2(y, x))
    print(lat,lon)
    return lat, lon


#Convert UTM information into latitude and longitude
def UTMToLatLon(easting:float, northing:float,zoneNumber: int, zoneLetter:str):
    loc = utm.to_latlon(easting, northing,zoneNumber, zoneLetter)
    print(loc)
    return loc

#Convert Latitude and Longitutde to UTM information
def LatLonToUTM(latitude: float, longitude: float):
    loc = utm.from_latlon(latitude, longitude)
    print(loc)
    return loc

print(round(DistanceBetweenTwoPoints(37.2279,77.4019,38.9907,77.0261)))
UTMToLatLon(713094, 4122654, 43, 'S')
ConvertToXYZ(-0.23391677292326765, 97.68132645835831)
XYZToLongLat(-851.5611645575466, 6313.77922072286, -26.010286150422274)
LatLonToUTM(37.2279, 77.4019)
