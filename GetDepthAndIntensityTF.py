import csv
import bagpy
from sensor_msgs import point_cloud2

def GetDepthandIntensityTransforms(robotName: str, bagFile):
    fields = ["X", "Y", "Z", "ROTX", "ROTY", "ROTZ", "ROTW", "TIME"]
    x = []
    y = []
    z = []
    rotx = []
    roty = []
    rotz = []
    rotw = []
    time = []

    csvFileName = 'DepthAndIntensityTransform.csv'
    with open(csvFileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for topic, msg, t in bagFile.read_messages(topics=[f'/tf']):
            for msg_tf in msg.transforms:
                translationX = msg_tf.transform.translation.x
                x.append(translationX)
                translationY = msg_tf.transform.translation.y
                y.append(translationY)
                translationZ = msg_tf.transform.translation.z
                z.append(translationZ)
                rotationX = msg_tf.transform.rotation.x
                rotx.append(rotationX)
                rotationY = msg_tf.transform.rotation.y
                roty.append(rotationY)
                rotationZ = msg_tf.transform.rotation.z
                rotz.append(rotationZ)
                rotationW = msg_tf.transform.rotation.w
                rotw.append(rotationW)
                timeS = t.secs
                time.append(timeS)
                
                
        colums = {}
        colums['X'] = x
        colums['Y'] = y
        colums['Z'] = z
        colums['ROTX'] = rotx
        colums['ROTY'] = roty
        colums['ROTZ'] = rotz
        colums['ROTW'] = rotw
        colums['TIME'] = time
        
        rows = zip(colums['X'],colums['Y'], colums['Z'],colums['ROTX'],colums['ROTY'],colums['ROTZ'],colums['ROTW'], colums['TIME'])
        
        csvwriter.writerows(rows)
