import os
import os
import shutil
source=input("enter the source folder")
destination=input("enter the destination")
source=source+'/'
destination=destination+'/'
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)