import torch
import torchvision
import torchvision.transforms as transforms
from pathlib import Path
from PIL import Image
import cv2
import os
import numpy as np
import PIL
from torchvision.utils import save_image
from PIL import Image, ImageOps



#convert to grayscale and 32 x 32 size
def ImageConversion(image: str, filename):
    im1 = Image.open(image)
    im2 = ImageOps.grayscale(im1)
    newsize = (32,32)
    im2 = im2.resize(newsize)
    im2.save(filename)
    
#convert to pytorch tensor and make it tensor grayscale
def ConvertImageTo2DTensor():
    # Define a transform to convert the image to tensor
    transform = transforms.ToTensor()
    transformGrayscale = transforms.Grayscale()
    transformResize = transforms.Resize((32,32))
    PILtransform = transforms.ToPILImage()
    imagePath = "/home/dominic/Downloads/Project/imgs/"
    os.chdir(imagePath)
    #image = format image and open it
    #path = f"{image}"
    
    for x in os.listdir():
        if x.endswith(".png"):
            openImage = Image.open(x)
            #print(list(openImage.getdata()))
            #openImage = transformGrayscale(openImage)
            #openImage = transformResize(openImage)
            #openImage.show()
            # Convert the image to PyTorch tensor
            twoDimensional = transform(openImage)
            twoDimensional2 = transformGrayscale(twoDimensional)
            print(twoDimensional2.ndimension())

            #this made the 3d image into a 2D image
            #twoDimensional = twoDimensional.permute(0,2,1)#[:, -1, :]
            
            #finds the max and min value in the tensor
            #mininumTensor = torch.amax(twoDimensional)
            #maximumTensor = torch.amin(twoDimensional)

            x2 = twoDimensional2
            #this made the tensor function into a 1D image
            #oneDimensional = torch.flatten(twoDimensional)
            openImage = x2[0]
            
            scaleup = x2.cpu().detach().numpy()[0]
            img = Image.fromarray(np.array([ x * 255 for x in scaleup]))
            if img.mode != 'RGB':
                img = img.convert('RGB')
                print(img)
            img.save(x, format='PNG')
            

ConvertImageTo2DTensor()
