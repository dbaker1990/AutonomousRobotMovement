import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import glob
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

class LidarDataset():
    def __init__(self, dataset, transforms, dataset_path, labels):
        self.dataset_path = "./dataset/"
        self.dataset = dataset
        file_list = glob.glob(self.dataset_path + "*")
        self.transforms = transforms
        self.labels = labels
        self.data = []
        
        for class_path in file_list:
            class_name = class_path.split("/")[-1]
            for dataset_path in glob.glob(class_path + "/*.jpeg"):
                self.data.append([dataset_path, class_name])
        print(self.data)
        
    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        #extracting image from index and scaling
        image = self.dataset[idx][0]
        #extracting label from index
        label = torch.tensor(self.dataset[idx][1])
        # applying transforms if transform is supplied
        if self.transforms:
            image = self.transforms(image)
        return (image, label)