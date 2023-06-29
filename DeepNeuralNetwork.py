import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import DeepNeuralNetworkTrainingModel

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        
        #1 input the image channel, 6 output channels, 5x5 square convolution
        self.conv1 = nn.Conv2d(1,6,5)
        self.conv2 = nn.Conv2d(6,16,5)
        
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16*5*5,120)# 5*5 from image dimension
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84, 10)
        
    def forward(self, x):
        #max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        
        # if the size is a square, you can specify with a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        
        x = torch.flatten(x, 1) # flatten all dimensions except the batch dimensions
        
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    

#important variables for the neural network
learning_rate = 0.01

net = Net()
#print(net)

#this is a test. it tests the learnable parameters of a model that is returned by the net.parameters()
params = list(net.parameters())
#print(len(params))
#print(params[0].size())

#random input that have a input size of 32x32.
input = torch.randn(1,1,32,32)
out = net(input)
#print(out)

#zero the gradient buffers on all parameters and backproops with random gradients
net.zero_grad()
out.backward(torch.randn(1,10))



#This area will define the loss functions
output = net(input)
target = torch.randn(10) # dummy target
target = target.view(1,-1) # make it the shame shape as the output
criterion = nn.MSELoss()

loss = criterion(output, target)
#print(loss)

#print(loss.grad_fn)  # MSELoss
#print(loss.grad_fn.next_functions[0][0])  # Linear
#print(loss.grad_fn.next_functions[0][0].next_functions[0][0])  # ReLU


#This are will be the backprop.
net.zero_grad() #zeroes the gradient buffers of all parameters

print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)

loss.backward()

print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

#This section will update the weights of the network

#this is the rule used in Stochastic Gradient Descent
#weight = weight - learning_rate * gradient

for f in net.parameters():
    f.data.sub_(f.grad.data * learning_rate)
    
#create the optimizer
optimizer = optim.SGD(net.parameters(), lr=0.01)

#this belongs in the training loop
optimizer.zero_grad() # zero the gradient buffers
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step() # this does the update

