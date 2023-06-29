import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
from torchvision.io import read_image
from torch.utils.data import DataLoader
from torchvision import datasets
import torchvision.transforms as transforms
from torchvision.transforms import ToTensor
import ConvolutionalNeuralNetwork
import LidarDataset
import os

# number of items in the dataset
batch_size = 128

#number of classes
num_classes = 1

#parameter of optimizer
learning_rate = 0.001

#number of times all training data is used to update the parameters
num_epoches = 20

#Determine the type of device being used. Either GPU or CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#Use the transforms.compose to reformat images for modeling
#save to variable all transforms for later use
all_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.4914, 0.4822, 0.4465],
                         std=[0.2023, 0.1994, 0.2010])
])

#create the dataset for training and validation
#These was just test data to make sure I had everything correct
#training_set = torchvision.datasets.FashionMNIST('./data', train=True, transform=transform, download=True)
#validation_set = torchvision.datasets.FashionMNIST('./data', train=False, transform=transform, download=True)
#This is the correct line. Just need to make a custom dataset
#training_set = torch.utils.DataLoader('./dataset', train=True, transform=all_transform, download=False)
#validation_set = torch.utils.DataLoader('./dataset', train=False, transform=all_transform, download=False)

#Create data loaders for dataset; shuffle for training, not for validation
#These was just test data to make sure I had everything correct
#training_loader = torch.utils.data.DataLoader(training_set, batch_size = Batch_Size, shuffle= True)
#validation_loader = torch.utils.data.DataLoader(validation_set, batch_size = Batch_Size, shuffle=True)

#training_loader = DataLoader(training_set, batch_size=batch_size, shuffle=True)
#validation_loader = DataLoader(validation_set, batch_size=batch_size, shuffle=True)

# Class labels
#add the different data classes so the model can learn what the different classes are
labels = (
    'Lidar',
)

# report the split size of the data
#print('Training set has {} instances'.format(len(training_set)))
#print('Validation set has {} instances'.format(len(validation_set)))
#turn 2d list to an object

model = ConvolutionalNeuralNetwork.ConvNeuralNet(num_classes)

# Set Loss function with criterion
criterion = nn.CrossEntropyLoss()

# Set optimizer with optimizer
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, weight_decay=0.005, momentum=0.9)

#inside the length addd the training loader
""" Uncomment this when ready
tal_step = len(training_loader)

# Use the pre-defin number of epochs to determine how many iterations to train the network on
for epoch in range(num_epoches):
    for i, (images, labels) in enumerate(training_loader):
        
        #move tensors to the configure device
        images = images.to(device)
        labels = labels.to(device)
        
        #Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epoches, loss.item()))"""