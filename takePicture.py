import cv2

cam = cv2.VideoCapture(0)
if(cam.IsOpened()):
    frame = cam.read()
    cap.Release()
    cv2.imwrite('test.jpg', frame)

