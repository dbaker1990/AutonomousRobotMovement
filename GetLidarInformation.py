import sys
import os
import csv
import rosbag
import rospy
import numpy as np
import open3d as o3d
import bagpy
from bagpy import bagreader
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from rosbags.image import message_to_cvimage
from PIL import Image as im
import cv2
import time
import ImageProcessing


def GetLidarInfo(directories: str, fileNames: str, robotName: str):
    fields = ["X", "Y", "Z", "Intensity", "Ring", "Time"]

    csvFileName = "Lidar_Information.csv"

    fileName = fileNames
    directory = directories
    results = directory + fileName
    extension = ".bag"
    bag = rosbag.Bag(directory+fileName+extension)


    #export lidar information based on x, y, z, intensity, ring, and time to a csv file
    with open(csvFileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        for topic, msg, t in bag.read_messages(topics=[f'/{robotName}/lidar_points']):
            cloud_points = list(point_cloud2.read_points(msg, skip_nans=True, field_names = ("x", "y", "z", 'intensity','ring','time')))
            csvwriter.writerows(cloud_points)
        
        