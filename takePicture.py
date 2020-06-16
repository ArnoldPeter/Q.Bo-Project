import cv2
from datetime import datetime

now = datetime.now()
file_name = now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
print(file_name)
cam = cv2.VideoCapture(0)
# 3 =  Enum for Picture Width
cam.set(3,1080)
# 4 = Enum for Picture Height
cam.set(4,720)
if cam.isOpened():
    _,frame = cam.read()
    cam.release()
    cv2.imwrite(file_name, frame)    