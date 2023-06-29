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
import tf


fileName = "upstairs_hallway_and_office_1_robot_10"
directory = "/home/dominic/Downloads/Project/RosBags/"
results = directory + fileName
extension = ".bag"
bag = rosbag.Bag(directory+fileName+extension)

for topic, msg, t in bag.read_messages(topics=['/tf']):
     #print(listener.subscription_callback(msg))
     info = msg._has_header
     
print(dir(info))