import sys
import FolderCheck
import Handle_ROS_Files
from pathlib import Path
import DistanceConversion
import ConvertBagVideoToImages
import GetLidarInformation
import GetOdometeryData

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
#These are optional variables. They are only good for certain function calls.s
count = 0
rosBagList = []

#convert bag videos to images and turns them into tensor grayscale
#ConvertBagVideoToImages.conversion(robotName, filenameToConvert, directory)

#Create the CSV file for Lidar Data
#GetLidarInformation.GetLidarInfo(directory,filenameToConvert,robotName)

#If needed this gets all the Ros Bags that's in the directory. Just uncomment if needed
#Handle_ROS_Files.GetBagsFromDirectory(directory, rosBagList)
#print(rosBagList[1])
#for i in rosBagList:
#    print(rosBagList[count])
#    count = count + 1

#This just calls the Distance Conversion file. Add the . to see all the functions that you possible would need
#DistanceConversion

GetOdometeryData.fileName = "upstairs_hallway_and_office_1_robot_10"
GetOdometeryData.GetMapToOdomTranslationAndRotation()
print(GetOdometeryData.translationXList[1])
print(GetOdometeryData.translationYList[1])
print(GetOdometeryData.translationZList[1])
#GetOdometeryData.AddInformationToCSVFile(GetOdometeryData.translationXList,GetOdometeryData.translationYList, GetOdometeryData.translationZList,GetOdometeryData.rotationXList,GetOdometeryData.rotationYList,GetOdometeryData.rotationZList,GetOdometeryData.rotationWList)

