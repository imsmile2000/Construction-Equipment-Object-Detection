import shutil
import os
file="C:/Users/yoonpyo/Desktop/root.txt"
source='C:/Users/yoonpyo/Desktop/acid_original/train/'
destination='C:/Users/yoonpyo/Desktop/1.17추가 데이터셋/acid7000.v2i.darknet/train/'
with open(file) as f:
    lines=f.read().splitlines()
for i in lines:
    if i in os.listdir("C:/Users/yoonpyo/Desktop/acid_original/train/"):
        shutil.move(source+i,destination)
