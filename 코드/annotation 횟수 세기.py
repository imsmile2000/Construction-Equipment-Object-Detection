import os
import glob
numbers=[0,0,0,0,0]
for filename in glob.glob('C:/Users/yoonpyo/darknet-master/data/images/dataset/train\*.txt'):
   with open(os.path.join('C:/Users/yoonpyo/darknet-master/data/images/dataset/train', filename), 'r') as f:
       text = f.readlines()
       for i in range(len(text)):
        #    print(text[i][0])
           if text[i][0]=='0':
                numbers[0]+=1
           elif text[i][0]=='1':
                numbers[1]+=1
           elif text[i][0]=='2':
                numbers[2]+=1
           elif text[i][0]=='3':
                numbers[3]+=1
           elif text[i][0]=='4':
                numbers[4]+=1
for i in range(5):
    print(numbers[i])