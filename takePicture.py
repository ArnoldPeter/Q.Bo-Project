import cv2
from datetime import datetime
import os
import schedule
import time

def MakePicture():
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
            file_name = now.strftime('%m_%d_%Y.%H_%M_%S') + '.jpg'
            os.chdir(imagepath)
            issaved = cv2.imwrite(file_name, frame)
            if issaved:
                print("Image " + file_name + " stored in " + imagepath + "!")
            else:
                print('An error has occured! Image hasnt been stored ! ')
            cv2.destroyAllWindows()
        else:
            print("Directory " + imagepath +" doesn't exist!")
            os.mkdir(imagepath)
            print("Directory " + imagepath +" has been made! ")
            file_name = now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
            os.chdir(imagepath)
            issaved = cv2.imwrite(file_name, frame)
            if issaved:
                print("Image " + file_name + " stored in " + imagepath + "!")
            else:
                print('An error has occured! Image hasnt been stored ! ')
            cv2.destroyAllWindows()

schedule.every().day.at("15:23").do(MakePicture)
#schedule.every().day.at("9:00").do(MakePicture)
#schedule.every().day.at("18:30").do(MakePicture)

while True:
    schedule.run_pending()
    time.sleep(1)

        