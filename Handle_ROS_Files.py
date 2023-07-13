import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import rosbag
import os

rosBagList = []
path = "/home/dominic/Downloads/Project/RosBags/2023-07-11-16-44-25.bag"

#convert ROS image messages to OpenCV images
def convert_depth_image(ros_image):
        cv_bridge = CvBridge()
        try:
            depth_image = cv_bridge.imgmsg_to_cv2(ros_image, desired_encoding='passthrough')
        except CvBridgeError:
            print()
        depth_array = np.array(depth_image, dtype=np.float32)
        np.save("depth_img.npy", depth_array)
        rospy.loginfo(depth_array)
        #To save image as png
        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        cv2.imwrite("depth_img.png", depth_colormap)
        #Or you use 
        # depth_array = depth_array.astype(np.uint16)
        # cv2.imwrite("depth_img.png", depth_array)


def pixel2depth(robotName):
    rospy.init_node('pixel2depth',anonymous=True)
    rospy.Subscriber(f"./{robotName}/camera/depth/image_raw", Image,callback=convert_depth_image, queue_size=1)
    rospy.spin()

#this functions gets a bag list and adds it to the list that holds the bag files
def GetRosBag(x):
    bag = rosbag.Bag(x)
    rosBagList.append(bag)

def GetBagsFromDirectory(directories: str, RosBagList: list):
    directory = directories
    for file in os.listdir(directory):
        bag = rosbag.Bag(directory + file)
        RosBagList.append(bag)
