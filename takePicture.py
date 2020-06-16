import cv2

cam = cv2.VideoCapture()
if(cam.IsOpened()):
    makePicture(cam)
else:
    #Say somethings wrong with the camera or try to open the camera



def makePicture(cam):
    cam.set(3,1080)
    cam.set(4,720)
    frame = cam.read()
    cam.Release()
    cv2.imwrite('test.jpg', frame)
    

    