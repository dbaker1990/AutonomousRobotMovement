import sys
import FolderCheck
import Handle_ROS_Files
from pathlib import Path
import DistanceConversion
import ConvertBagVideoToImages
import GetLidarInformation
import GetOdometeryData
import rosbag
from pandas import *
import ImageProcessing

#checks to see if you have the neccessary paths. Do not Delete this. It detects all neccesarry folders that is needed for this project to run
a =  FolderCheck.CheckIfNecessaryDirectoryExists()

#if all the folders exists do nothing. But it tells you the first folder it is missing and then closes the program
if a == True:
    print()
else:
    sys.exit(0)


#Directory and common variables in Project. So it can be modular
directory = "./RosBags/"
filenameToConvert = "upstairs_hallway_and_office_1_robot_10"
robotName = "sekhmet"
#These are optional variables. They are only good for certain function calls
count = 0
rosBagList = []

#Open Bag file
bag = rosbag.Bag(directory+filenameToConvert+".bag")




#DO NOT CHANGE the order of how these classes are called. They need to be called in this order in order to function correctly.





#Create the CSV file for Lidar Data
GetLidarInformation.GetLidarInfo(directory,filenameToConvert,robotName, bag)

#If needed this gets all the Ros Bags that's in the directory. Just uncomment if needed
#Handle_ROS_Files.GetBagsFromDirectory(directory, rosBagList)
#print(rosBagList[1])
#for i in rosBagList:
#    print(rosBagList[count])
#    count = count + 1

#This just calls the Distance Conversion file. Add the . to see all the functions that you possible would need
#DistanceConversion

GetOdometeryData.fileName = filenameToConvert
GetOdometeryData.GetMapToOdomTranslationAndRotation(bag)
GetOdometeryData.AddInformationToCSVFile(GetOdometeryData.translationXList,GetOdometeryData.translationYList, GetOdometeryData.translationZList,GetOdometeryData.rotationXList,GetOdometeryData.rotationYList,GetOdometeryData.rotationZList,GetOdometeryData.rotationWList)
GetOdometeryData.GetTimeStamps(bag)
GetOdometeryData.MapToOdomTimeStampToCSV()


#convert bag videos to images and turns them into tensor grayscale
ConvertBagVideoToImages.conversion(robotName, filenameToConvert, directory,bag)
bag.close()

