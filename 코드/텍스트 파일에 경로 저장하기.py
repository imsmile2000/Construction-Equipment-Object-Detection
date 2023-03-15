import glob
image_directory = "A:/technonia_darknet yolo/test/"
extension = "*.txt"
save_at = "A:/technonia_darknet yolo//test2.txt"
files = sorted(glob.glob(image_directory + extension))
for file in files:
    f = open(save_at, 'a')
    f.write(file + "\n")
    print(file)