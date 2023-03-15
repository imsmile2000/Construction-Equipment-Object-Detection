import shutil
import os
file="A:/technonia_darknet yolo/test2.txt"
source='A:/technonia_darknet yolo/test/'
destination='A:/technonia_darknet yolo/'
with open(file) as f:
    lines=f.read().splitlines()
for i in lines:
    if i in os.listdir("A:/technonia_darknet yolo/test"):
        shutil.move(source+i,destination)