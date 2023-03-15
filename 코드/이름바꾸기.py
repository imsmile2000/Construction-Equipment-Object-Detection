import os
import shutil
file_path = 'C:/Users/yoonpyo/darknet-master/data/images/data416/test'
file_names = os.listdir(file_path)
for name in file_names:
    src=os.path.join(file_path,name)
    dst=name[0:6]+".jpg"
    dst=os.path.join(file_path,dst)
    shutil.move(src,dst)