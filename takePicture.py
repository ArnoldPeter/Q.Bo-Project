import cv2
from datetime import datetime
import os
import schedule
import time

# def MakePicture():
#     cam = cv2.VideoCapture(0)
#     cam.set(3, 320) 
#     cam.set(4, 240)
#     if cam.isOpened():
#         _,frame = cam.read()
#         now = datetime.now()
#         cam.release()
#         currentDirectory = os.curdir()
#         print(currentDirectory)
#         imagepath = currentDirecotry + "\Images"
#         print(imagepath)
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
    config = yaml.safe_load(open("opt/qbo/config.yml"))
    cam = cv2.VideoCapture(int(config['camera']))
    cam.set(3, 320) 
    cam.set(4, 240)
    path = "/Tmp/"
    now = datetime.now()
    fullPath = path + now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
    if(os.path.exists(path)):
        print("Directory existed!")
        _, frame = cam.read()
        cam.release()
        cv2.imwrite(fullPath, frame)
        print("Saved Picture!")
    else:
        os.mkdir(path)
        _, frame = cam.read()
        cam.release()
        cv2.imwrite(fullPath, frame)


# def MakePictureWithEmail():
#     #Get config file
#     config = yaml.safe_load(open("/opt/qbo/config.yml"))
#     #Set Camera and get Cameraindex from config 
#     cam = cv2.VideoCapture(int(config['config.yml']))
#     #Set Camera Width on 320
#     cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320) 
#     #Set Camera Hight on 240
#     cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
#     #If camera is opened and ready
#     if cam.isOpened():
#         #Read Frame/take Picture
#         _, frame = cam.read()
#         #Get current Time
#         now = datetime.now()
#         #Get FileName from current Time
#         file_name = now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
#         #Release camera
#         cam.release()
#         #Write frame into file
#         cv2.imwrite(file_name,frame)
#         #Send Email file to "qbo.prototyp@gmail.com"
#         #when finished => 
#         #os.remove(file_name)

MakePicture()