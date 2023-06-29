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


fields = ["X", "Y", "Z", "Intensity", "Ring", "Time"]

csvFileName = "Lidar_Information.csv"

fileName = "upstairs_hallway_and_office_1_robot_10"
directory = "/home/dominic/Downloads/Project/RosBags/"
results = directory + fileName
extension = ".bag"
bag = rosbag.Bag(directory+fileName+extension)
saveImagePath = "/home/dominic/Downloads/Project/imgs"
saveImageFileName = ""
extenstion2 = ".png"

os.chdir(saveImagePath)
# Get all message on the /joint states topic
with open(csvFileName, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for topic, msg, t in bag.read_messages(topics=['/sekhmet/camera/image_raw']):
        info = dir(msg)
        img = message_to_cvimage(msg)
        img = message_to_cvimage(msg, 'bgr8')
        new_im = im.fromarray(img)
        new_im = np.asarray(img)
        timeStamp = time.time()
        saveImageFileName = str(timeStamp)
        cv2.imwrite(saveImageFileName + extenstion2, new_im)
        ImageProcessing.ImageConversion(saveImagePath+"/"+saveImageFileName+extenstion2, saveImageFileName+extenstion2)
bag.close()
