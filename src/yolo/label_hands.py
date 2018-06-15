import cv2;
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torch.utils.data import sampler

import torchvision.datasets as dset
import torchvision.transforms as T

import numpy as np
import json

with open('annotation.json') as data_file:
    data = json.load(data_file)
    
path = 'E:/hand_pose/Dataset/hands/'

for name in data:
    min_y = data[name][0][1]
    max_y = data[name][0][1]
    min_x = data[name][0][0]
    max_x = data[name][0][0]
    
    for pair in data[name]:
        if pair[1] < min_y:
            min_y = pair[1]
        if pair[1] > max_y:
            max_y = pair[1]
        if pair[0] < min_x:
            min_x = pair[0]
        if pair[0] > max_x:
            max_x = pair[0]
    if (not(name[:3]=='001' or name[:3]=='000' or name[:3]=='002')):
        continue
    
    file_name = name[:-2]+".jpg"
    full_path = path+file_name
    img = cv2.imread(full_path)
    
    y_add = 200-(int(max_y)-int(min_y))
    x_add = 200-(int(max_x)-int(min_x))

    min_x = int(min_x)
    min_y = int(min_y)
    max_x = int(max_x)
    max_y = int(max_y)
    
    if y_add % 2 == 0:
        y_cord_min = max(0,min_y - int(y_add/2))
        y_cord_max = min(1080,max_y + int(y_add/2))

    else:
        y_cord_min = max(0,min_y - (1+int(y_add/2)))
        y_cord_max = min(1080,max_y + int(y_add/2))

    if x_add % 2 == 0:
        x_cord_min = max(0,min_x - int(x_add/2))
        x_cord_max = min(1920,max_x + int(x_add/2))

    else:
        x_cord_min = max(0,min_x - (1+int(x_add/2)))
        x_cord_max = min(1920,max_x + int(x_add/2))
    
    pixels = "1\n%d %d %d %d" % (y_cord_min,y_cord_max,x_cord_min,x_cord_max)
    output = "E:/hand_pose/Dataset/handslabel/"+name[:-2]+".txt"
    if (name[-1]=='R'):
        file = open(output,'w')
    elif (name[-1]=='L'):
        file = open(output,'a')
    
    file.write(pixels)
    file.close()
    cv2.waitKey(0)
    cv2.destroyAllWindows()