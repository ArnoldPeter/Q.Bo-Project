import cv2
from datetime import datetime
import os
import schedule
import time
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
        #Sends Mail to the drive
        SendMail(fullPath)
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
        #Sends Mail to the drive
        SendMail(fullPath)
        #Delete the picture
        os.remove(fullPath)
        print("Picture deleted! ")

def SendMail(fullpath):
    #Email user name
    email_user = 'qbo.prototyp@gmx.at'
    #email password
    email_pw = 'FHWN2700'
    #binary data of the to be sended picture
    img_data = open(fullpath, 'rb').read()
    print("Opened Picture")
    #Create message
    msg = MIMEMultipart()
    #Get current daytime
    now = datetime.now()
    #Set the Subject to the current time
    msg['Subject'] = now.strftime("%m_%d_%Y.%H_%M_%S")
    #Set the email which the email is form
    msg['From'] = 'qbo.prototyp@gmx.at'
    #Set the email which the email goes to
    msg['To'] = 'qbo.prototyp@gmail.com'
    print("Header Created")

    #Create text in the email
    text = MIMEText("Photo taken by the Q.Bo Robot at " + now.strftime("%m_%d_%Y.%H_%M_%S") + "local day time! ")
    #Attach it to the email
    msg.attach(text)
    print("Image created!")
    #Get the picture and attach it to the email
    image = MIMEImage(img_data, name=os.path.basename(fullpath))
    msg.attach(image)

    print("Logging into GMX! ")
    #Get the smtp data of the email server
    s = smtplib.SMTP('smtp.gmx.net',587)
    s.ehlo()
    #connect to server
    s.starttls()
    s.ehlo()
    #Login with the necessary email data
    s.login(email_user,email_pw)
    #Send the mail
    s.sendmail('qbo.prototyp@gmx.at','qbo.prototyp@gmail.com',msg.as_string())
    #Quit the mailwriting
    s.quit
    print("Sent!")

MakePicture()