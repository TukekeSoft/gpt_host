import serial
ser = serial.Serial('/dev/ttyACM0', 4800,timeout=10)  # open first serial port
print ser.name          # check which port was really used
ser.write("1234ABCDEFGHIJKLMNOP")      # write a string
while 1:
	flag = ser.read()
	if flag == '=':
		s = ser.read(20)
		break
#//s = ser.read(x)    
print s
import os
os.system("gvimdiff&")
ser.close()             # close port
