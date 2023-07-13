import os
import numpy as np
import ImageProcessing
from rosbags.image import message_to_cvimage
import cv2
import time


def ConvertDepthVideoToImages(bagFile, robotName: str):
    saveImagePath = "/home/dominic/Downloads/Project/imgs/depth"
    saveImageFileName = ""
    extenstion2 = ".tiff"

    os.chdir(saveImagePath)
    
    for topic, msg, t in bagFile.read_messages(topics= [f'/{robotName}/img_node/range_image']):
        img = message_to_cvimage(msg, 'bgr8')
        new_im = np.asarray(img)
        timeStamp = time.time()
        saveImageFileName = str(timeStamp)
        cv2.imwrite(saveImageFileName + extenstion2, new_im)
        #ImageProcessing.ImageConversion(saveImagePath+"/"+saveImageFileName+extenstion2, saveImageFileName+extenstion2)
    
    ImageProcessing.ConvertImageTo2DTensor()
    

def ConvertIntensityVideoToImages(bagFile, robotName: str):
    saveImagePath = "/home/dominic/Downloads/Project/imgs/intensity"
    saveImageFileName = ""
    extenstion2 = ".tiff"

    os.chdir(saveImagePath)
    
    for topic, msg, t in bagFile.read_messages(topics= [f'/{robotName}/img_node/intensity_image']):
        img = message_to_cvimage(msg, 'bgr8')
        new_im = np.asarray(img)
        timeStamp = time.time()
        saveImageFileName = str(timeStamp)
        cv2.imwrite(saveImageFileName + extenstion2, new_im)
        #ImageProcessing.ImageConversion(saveImagePath+"/"+saveImageFileName+extenstion2, saveImageFileName+extenstion2)
    
    ImageProcessing.ConvertImageTo2DTensor()
    
def ConvertAmbientVideoToImages(bagFile, robotName: str):
    saveImagePath = "/home/dominic/Downloads/Project/imgs/ambient"
    saveImageFileName = ""
    extenstion2 = ".tiff"

    os.chdir(saveImagePath)
    
    for topic, msg, t in bagFile.read_messages(topics= [f'/{robotName}/img_node/ambient_image']):
        img = message_to_cvimage(msg, 'bgr8')
        new_im = np.asarray(img)
        timeStamp = time.time()
        saveImageFileName = str(timeStamp)
        cv2.imwrite(saveImageFileName + extenstion2, new_im)
        #ImageProcessing.ImageConversion(saveImagePath+"/"+saveImageFileName+extenstion2, saveImageFileName+extenstion2)
    
    ImageProcessing.ConvertImageTo2DTensor()