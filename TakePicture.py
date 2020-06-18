import cv2
import yaml
from datetime import datetime

config = yaml.safe_load(open("/opt/qbo/config.yml"))


def makepicture():
    cam = cv2.VideoCapture(int(config['camera']))
    # 3 =  Enum for Picture Width
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)  # I have found this to be about the highest-
    cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

    if cam.isOpened():
        _, frame = cam.read()
        now = datetime.now()
        file_name = now.strftime("%m_%d_%Y.%H_%M_%S") + ".jpg"
        cam.release()
        cv2.imwrite(file_name, frame)