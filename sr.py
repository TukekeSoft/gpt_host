import serial
import numpy
ser = serial.Serial('/dev/ttyACM0', 4800,timeout=10)  # open first serial port
print ser.name          # check which port was really used
raw_input()
ser.write(" ");
raw_input();
s=[]
ser.write("1234ABCDEFGHIJKLMNOP")      # write a string
#while 1:
for i in range(1,20):
	s.append(ser.read(1))
#flag = ser.read()
#	if flag == '=':
#s = ser.read(20)
#		break
#s = ser.read(x)    
s1="012345678901234567890"

print s1
print s
a=[]
a1=[]
for i in range(1,20):
	a[i] = s[i];
	a1[i] = s1[i];


x = numpy.array(a);
x1 = numpy.array(a1);

numpy.savetxt("source.csv", x, delimiter=",")
numpy.savetxt("test.csv", x1, delimiter=",")

import os
os.system("gvimdiff source.csv,test.csv&")
#ser.close()             # close port
