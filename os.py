import os 
import shutil
print(dir(os))
# os.getcwd()
#os.mkdir("102")
os.listdir()
path = "102"
print("before copying files:")

source= "feather.jfif"
destination = "102/feather.jfif"
shutil.copy(source,destination)
print("after copying file:")
print(os.listdir(path))
