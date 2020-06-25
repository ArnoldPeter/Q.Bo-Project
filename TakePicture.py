import time
import serial
from controller.QboController import Controller

port = '/dev/serial0'
ser = serial.Serial(port, baudrate=115200, bytesize = serial.EIGHTBITS, stopbits = serial.STOPBITS_ONE, parity = serial.PARITY_NONE, rtscts = False, dsrdtr =False, timeout = 0)
QBO = Controller(ser)

time.sleep(5)
QBO.SetServo(1,511, 100)#Axis,Angle,Speed
QBO.SetServo(2,450,100)#Axis,Angle,Speed
time.sleep(5)
QBO.SetServo(1,715, 100)#Axis,Angle,Speed
time.sleep(5)
QBO.SetServo(1,511, 100)#Axis,Angle,Speed
time.sleep(5)
QBO.SetServo(1,300, 100)#Axis,Angle,Speed
time.sleep(5)
QBO.SetServo(1,511, 100)#Axis,Angle,Speed
