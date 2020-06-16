import cv2

cam = cv2.VideoCapture()
if(cam.IsOpened()):
    frame = cam.read()
    cam.Release()
    cv2.imwrite('test.jpg', frame)
