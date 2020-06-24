import os
import shutil
import schedule
import time
from datetime import datetime

def CreateFolder():
    #Gets Folder String from other method
    foldername = GetDirectoryPath()
    #Checks if the Folder does not exists
    if not os.path.exists(foldername):
        #Creates the fodler
        os.mkdir(foldername)
        print("Folder created! ")
        #Returnes the name of the folder
        return foldername
    #If The folder exists
    else:
        print("Folder has existed! ")
        #Returnes the name of the folder
        return foldername

def GetDirectoryPath():
    #Get current day time
    now = datetime.now()
    #Create Folder Name
    Foldername = now.strftime("%m_%d_%Y")
    print("Folder String created : " + Foldername)
    return Foldername

def MoveFile(fileName):
    #Finds the first dot in the string
    position = fileName.find('.')
    #Creates an empty string
    dayOfPicture = ""
    #Get the day of the picture
    for i in range(0,position):
        dayOfPicture += fileName[i]
    print("Date of the picture received! ")
    print(dayOfPicture)
    #Gets the folder name and checks if the folder is avaiable
    foldername = CreateFolder()
    print(foldername)
    #If the day of the picture and the folder name matches, the file will be moved
    if(dayOfPicture == foldername):
        #Move file to destination
        print("Moving File! ")
        shutil.move(fileName, foldername)
        print("File moved! ")

def FileWatcher():
    counter = 0
    while(counter < 21):
        print(str(counter) + " / " + str(20))
        #Changes directory to needed path
        os.chdir("C:\Users\Benjamin Moser\Google Drive")
        #Foreach file with the .jpg extension
        for file in os.listdir(os.curdir):
            if file.find(".jpg") > -1:
                #Move file to directory
                MoveFile(file)
        counter += 1
        #Sleeps 20 seconds per searching
        time.sleep(20)

FileWatcher()
