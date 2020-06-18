import cv2
from datetime import datetime
import os
import schedule
import time

# def MakePicture():
#     cam = cv2.VideoCapture(0)
#     cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320) 
#     cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
#     if cam.isOpened():
#         _,frame = cam.read()
#         now = datetime.now()
#         cam.release()
#         currentDirecotry = os.curdir()
#         imagepath = currentDirecotry
#         if(os.path.exists(imagepath)):
#             print("Directory Exists!")
#             file_name = now.strftime('%m_%d_%Y.%H_%M_%S') + '.jpg'
#             os.chdir(imagepath)
#             issaved = cv2.imwrite(file_name, frame)
#             if issaved:
#                 print("Image " + file_name + " stored in " + imagepath + "!")
#             else:
#                 print('An error has occured! Image hasnt been stored ! ')
#             cv2.destroyAllWindows()
#         else:
#             print("Directory " + imagepath +" doesn't exist!")
#             os.mkdir(imagepath)
#             print("Directory " + imagepath +" has been made! ")
#             file_name = now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
#             os.chdir(imagepath)
#             issaved = cv2.imwrite(file_name, frame)
#             if issaved:
#                 print("Image " + file_name + " stored in " + imagepath + "!")
#             else:
#                 print('An error has occured! Image hasnt been stored ! ')
#             cv2.destroyAllWindows()

def MakePicture():
    config = yaml.safe_load(open("/opt/qbo/config.yml"))
    cam = cv2.VideoCapture(int(config['config.yml']))
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320) 
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
    if cam.isOpened():
        _, frame = cam.read()
        now = datetime.now()
        file_name = now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
        cam.release()
        cv2.imwrite(file_name,frame)
        #Email file to "qbo.prototyp@gmail.com"
        #when finished
        #os.remove(file_name)
MakePicture()