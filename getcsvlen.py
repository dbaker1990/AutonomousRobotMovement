import csv
import bagpy
from sensor_msgs import point_cloud2


file = open("Lidar_Information.csv")
numline = len(file.readlines())
print(numline)