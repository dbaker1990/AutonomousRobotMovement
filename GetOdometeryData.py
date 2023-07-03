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
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
import tf2_py as tf2
import pandas as pd


fileName = "upstairs_hallway_and_office_1_robot_10"
directory = "./RosBags/"
results = directory + fileName
extension = ".bag"
bag = rosbag.Bag(directory+fileName+extension)

#Important Lists
translationXList = []
translationYList = []
translationZList = []
rotationXList = []
rotationYList = []
rotationZList = []
rotationWList = []
timestamp = []

tfListener = tf.Transformer(True, rospy.Duration(3600.0))

def GetBasicInformation(fileNames: str, directorys: str):
    fileName = fileNames
    directory = directorys
    results = directory + fileName + extension
    bag = rosbag.Bag(directory+fileName+extension)
    GetTimeStamps()
    

def GetMapToOdomTranslationAndRotation():
    for topic, msg, t in bag.read_messages(topics=['/tf']):
        for msg_tf in msg.transforms:
            helping = msg_tf
            translationX = msg_tf.transform.translation.x
            translationXList.append(translationX)
            translationY = msg_tf.transform.translation.y
            translationYList.append(translationY)
            translationZ = msg_tf.transform.translation.z
            translationZList.append(translationZ)
            rotationX = msg_tf.transform.rotation.x
            rotationXList.append(rotationX)
            rotationY = msg_tf.transform.rotation.y
            rotationYList.append(rotationY)
            rotationZ = msg_tf.transform.rotation.z
            rotationZList.append(rotationZ)
            rotationW = msg_tf.transform.rotation.w
            rotationWList.append(rotationW)
    bag.close()

def GetTimeStamps():
    for topic, msg, t in bag.read_messages(topics=['/tf']):
        timestamp.append(t.to_sec())

#Get all the infromation from the translation and rotation and put it inside of a csv file
def AddInformationToCSVFile(translationX: list, translationY: list, translationZ: list, rotationX: list, rotationY: list, rotationZ: list, rotationW: list):
    csvFileName = "OdomInformation.csv"
    fields = ["transX", "transY", "transZ", "rotX", "rotY", "rotZ", "rotW"]
    columns = {}
    columns["transx"] = translationXList
    columns["transy"] = translationYList
    columns["transz"] = translationZList
    columns["rotx"] = rotationXList
    columns["roty"] = rotationYList
    columns["rotz"] = rotationZList
    columns["rotw"] = rotationWList
    rows = zip(columns["transx"],columns["transy"],columns["transz"],columns["rotx"],columns["roty"],columns["rotz"], columns["rotw"])
    
    with open(csvFileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
