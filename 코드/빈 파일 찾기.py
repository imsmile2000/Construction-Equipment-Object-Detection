import glob
import os
for filename in glob.glob('C:/Users/yoonpyo/Desktop/1.17추가 데이터셋/acid7000.v2i.darknet/train\*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       text = f.read()
       ##f.write(text_mod)
       print(text)
           
       
