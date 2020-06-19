import cv2
from datetime import datetime
import os
import schedule
import time

def MakePicture():
    #Load config file
    config = yaml.safe_load(open("opt/qbo/config.yml"))
    #set camera and get camera index from config file
    cam = cv2.VideoCapture(int(config['camera']))
    #Set Camera Width on 320 pixels
    cam.set(3, 320) 
    #Set Camera Height on 240 pixels
    cam.set(4, 240)
    #Path to be written to
    path = "tmp/"
    #Get current day time
    now = datetime.now()
    #File name with the current time in the name
    file_name = now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
    #Full path with file and directory name
    fullPath = path + file_name
    #If Directory exists
    if(os.path.exists(path)):
        print("Directory existed! ")
        #Read a frame from the camera
        _, frame = cam.read()
        print("Picture has been taken! ")
        #Release the camera
        cam.release()
        #Write image into the file
        cv2.imwrite(fullPath, frame)
        print("Image has been created! ")
        #!
        #Email the picture to qbo.prototyp@gmail.com 
        #!
        #Sleep as long as the email needs access to the picture
        time.sleep(3)
        #Delete the picture
        os.remove(fullPath)
        print("Picture deleted! ")
    else:
        print("Directory does not exist! ")
        #Create the wanted Directory
        os.mkdir(path)
        print("Directory has been created! ")
        #Read a frame from the camera
        _, frame = cam.read()
        print("Picture has been taken! ")
        #Release the camera
        cam.release()
        #Write image into the file
        cv2.imwrite(fullPath, frame)
        print("Image has been created! ")
        #!
        #Email the picture to qbo.prototyp@gmail.com 
        #!
        #Sleep as long as the email needs access to the picture
        time.sleep(3)
        #Delete the picture
        os.remove(fullPath)
        print("Picture deleted! ")

MakePicture()