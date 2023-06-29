import torch
import numpy as np
from datetime import datetime
import sys
import os
import LidarDataset
import TrainingModule
import ImageProcessing
import FolderCheck
import Handle_ROS_Files
from pathlib import Path
import DistanceConversion
import ConvertBagVideoToImages
import GetLidarInformation
    
#checks to see if you have the neccessary paths
a =  FolderCheck.CheckIfNecessaryDirectoryExists()

if a == True:
    print()
else:
    sys.exit(0)

#Directory and common variables in Project. So it can be modular
directory = "./RosBags/"
filenameToConvert = "upstairs_hallway_and_office_1_robot_10"
robotName = "sekhmet"

#convert bag videos to images and turns them into tensor grayscale
ConvertBagVideoToImages.conversion(robotName, filenameToConvert, directory)

#Create the CSV file for Lidar Data
GetLidarInformation.GetLidarInfo(directory,filenameToConvert,robotName)

