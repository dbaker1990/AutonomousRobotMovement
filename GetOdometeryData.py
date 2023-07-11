import csv
import rosbag
import rospy
import bagpy
import tf


fileName = "upstairs_hallway_and_office_1_robot_10"
directory = "./RosBags/"

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
    results = directory + fileName + ".bag"
    bag = rosbag.Bag(directory+fileName+".bag")
    GetTimeStamps()
    

def GetMapToOdomTranslationAndRotation(bagFile: bagpy):
    for topic, msg, t in bagFile.read_messages(topics=['/tf']):
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
    

def GetTimeStamps(bagFile: bagpy):
    for topic, msg, t in bagFile.read_messages(topics=['/tf']):
        timestamp.append(t.to_sec())

#Get all the infromation from the translation and rotation and put it inside of a csv file
def AddInformationToCSVFile(translationX: list, translationY: list, translationZ: list, rotationX: list, rotationY: list, rotationZ: list, rotationW: list):
    csvFileName = 'MapToOdom.csv'
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

def MapToOdomTimeStampToCSV():
    cvsFileName = 'MapToOdomTimeStamp.csv'
    fields = ["Time Stamps"]
    columns = {}
    columns["Time Stamp"] = timestamp
    rows = zip(columns["Time Stamp"])
    
    with open(cvsFileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)