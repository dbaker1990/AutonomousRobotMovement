import torch
import numpy as np
from datetime import datetime
import sys
import LidarDataset
import TrainingModule
import ImageProcessing
import FolderCheck
import Handle_ROS_Files
from pathlib import Path
import DistanceConversion
    
#checks to see if you have the neccessary paths
a =  FolderCheck.CheckIfNecessaryDirectoryExists()

if a == True:
    print()
else:
    sys.exit(0)


#how to convert image to 1D. It calls a class I made.
ImageProcessing.ImageConversion('penguins.jpg')

DistanceConversion