txt = open('C:/Users/yoonpyo/darknet-master/data/list/valid0.txt','r')
f = open('C:/Users/yoonpyo/darknet-master/data/list/valid.txt','w')
while True :
    line = txt.readline()
    if not line:
        break
    f.write('Yolo_mark-master/'+line)
        
txt.close()
f.close()