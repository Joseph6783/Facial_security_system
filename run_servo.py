import serial
import time

def setAngle(ser, channel, angle):
    minAngle = 0.0
    maxAngle = 180.0
    minTarget = 256.0
    maxTarget = 13120.0
    scaledValue = int((angle/((maxAngle - minAngle) / (maxTarget - minTarget))) + minTarget)
    commandByte = chr(0x84)
    channelByte = chr(channel)
    lowTargetByte = chr(scaledValue & 0x7F)
    highTargetByte = chr((scaledValue >> 7) & 0x7F)
    command = commandByte + channelByte + lowTargetByte + highTargetByte
    ser.write(command)
    ser.flush()
    
# ser = serial.Serial("/dev/ttyACM0", 9600)
# servo = 0
# angle = 0
#     
# while(servo != 10):
#     #servo = int(raw_input("Servo: "))
#     angle = int(raw_input("Angle: "))
#     setAngle(ser, servo, angle)
#     