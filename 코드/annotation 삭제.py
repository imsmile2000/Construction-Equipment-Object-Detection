import os
import glob
for filename in glob.glob('C:/Users/yoonpyo/darknet-master/data/images/dataset/valid\*.txt'):
   with open(os.path.join('C:/Users/yoonpyo/darknet-master/data/images/dataset/valid', filename), 'r') as f:
       lines = f.readlines()
   with open(os.path.join('C:/Users/yoonpyo/darknet-master/data/images/dataset/valid', filename), 'w') as f:
       for line in lines:
           if line[0]!='0' and line[0]!='1':
               f.write(line)
   
                