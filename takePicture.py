import cv2
from datetime import datetime
import os

cam = cv2.VideoCapture(0)
# 3 =  Enum for Picture Width
cam.set(3,1080)
# 4 = Enum for Picture Height
cam.set(4,720)
if cam.isOpened():
    _,frame = cam.read()
    now = datetime.now()
    cam.release()
    imagepath = 'C:\Temp\Testing'
    if(os.path.exists(imagepath)):
        print("Directory Exists!")
        file_name = now.strftime("Images\%m_%d_%Y.%H_%M_%S") + ".jpg"
        file_path=os.path.join(imagepath,file_name)
        cam.release()
        cv2.imwrite(file_path, frame)
        cv2.destroyAllWindows()
    else:
        print("Directory doesn't exist!")
        os.mkdir(imagepath)
        print("Directory made! ")
        file_name = now.strftime("Images\%m_%d_%Y.%H_%M_%S") + ".jpg"
        cam.release()
        cv2.imwrite(os.path.join(imagepath, file_name), frame)
        cv2.destroyAllWindows()

        