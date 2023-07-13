import csv
import bagpy
from sensor_msgs import point_cloud2


file = open("DepthAndIntensityTransform.csv")
numline = len(file.readlines())
print(numline)