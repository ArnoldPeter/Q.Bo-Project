import cv2
from datetime import datetime
import os
import schedule
import time
<<<<<<< Updated upstream

def MakePicture():
    #Load config file
    config = yaml.safe_load(open("opt/qbo/config.yml"))
    #set camera and get camera index from config file
    cam = cv2.VideoCapture(int(config['camera']))
=======
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def MakePicture():
    # #Load config file
    # config = yaml.safe_load(open("opt/qbo/config.yml"))
    # #set camera and get camera index from config file
    # cam = cv2.VideoCapture(int(config['camera']))
    cam = cv2.VideoCapture(0)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        #Email the picture to qbo.prototyp@gmail.com 
=======
        SendMail(fullPath)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        #Email the picture to qbo.prototyp@gmail.com 
=======
        SendMail(fullPath)
>>>>>>> Stashed changes
        #!
        #Sleep as long as the email needs access to the picture
        time.sleep(3)
        #Delete the picture
        os.remove(fullPath)
        print("Picture deleted! ")

<<<<<<< Updated upstream
=======
def SendMail(fullpath):
    gmail_user = 'qbo.prototyp@gmail.com'
    gmail_pw = 'FHWN2700'
    img_data = open(fullpath, 'rb').read()
    print("Opened Picture")
    msg = MIMEMultipart()
    msg['Subject'] = 'Testing'
    msg['From'] = 'qbo.prototyp@gmail.com'
    msg['To'] = 'qbo.prototyp@gmail.com'
    print("Header Created")

    text = MIMEText("test")
    msg.attach(text)
    print("Image created!")
    image = MIMEImage(img_data, name=os.path.basename(fullpath))
    msg.attach(image)

    print("Logging into Google! ")
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(gmail_user,gmail_pw)
    s.send(From, To, msg.as_string())
    s.quit
    print("Sent!")

>>>>>>> Stashed changes
MakePicture()