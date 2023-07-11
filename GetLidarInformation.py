import csv
import bagpy
from sensor_msgs import point_cloud2




def GetLidarInfo(directories: str, fileNames: str, robotName: str, bagFile: bagpy):
    fields = ["X", "Y", "Z", "Intensity", "Ring", "Time"]

    csvFileName = 'Lidar_Information.las'


    #export lidar information based on x, y, z, intensity, ring, and time to a csv file
    with open(csvFileName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        for topic, msg, t in bagFile.read_messages(topics=[f'/{robotName}/lidar_points']):
            cloud_points = list(point_cloud2.read_points(msg, skip_nans=True, field_names = ("x", "y", "z", 'intensity','ring','time')))
            csvwriter.writerows(cloud_points)
        
        