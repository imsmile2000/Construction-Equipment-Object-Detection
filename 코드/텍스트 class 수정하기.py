import re
from msilib.schema import Directory
import os
directory=os.listdir('C:/Users/yoonpyo/Downloads/darknet/person.v1i.darknet/train')
os.chdir('C:/Users/yoonpyo/Downloads/darknet/person.v1i.darknet/train')
for file in directory:
    open_file=open(file,'r')
    read_file=open_file.read()
    regex=re.compile('0 ')
    read_file=regex.sub('4 ',read_file)
    write_file=open(file,'w')
    write_file.write(read_file)
       
