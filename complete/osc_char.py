import serial
import numpy
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
ser = serial.Serial('/dev/ttyACM0', 4800,timeout=10)  # open first serial port
print ser.name          # check which port was really used

val=[]
frequency=[]
bias=[]
#ser.write("1234ABCDEFGHIJKLMNOP")      # write a string

#while 1:
#	flag = ser.read()
#	if flag == 'G':
for i in range(0,24):
	ser.write('A')
	time.sleep(4)
	ser.write('A')
	temp = ser.read(1)
	val.append(ord(temp))
	byte1 = ord(ser.read(1))
	byte2 = ord(ser.read(1))
	#print 256*byte1 + byte2
	tbias = (256*byte1 + byte2)*1.8/4096
	bias.append(tbias)
	fm0 = ord(ser.read(1))
	fm1 = ord(ser.read(1))
	fm2 = ord(ser.read(1))
	#print i
	#freq = struct.pack(fm0,3)
	freq = (65536*fm2 + fm1*256 + fm0)/1
#freq = 16*510*freq
	#print fm2,fm1,fm0
	print freq
	frequency.append(freq)
	time.sleep(4)

print bias
print frequency
a = numpy.array([bias,frequency])
a = a.transpose()
frequency = a[:,1]/1e9
numpy.savetxt("LC_chars.csv", a, delimiter=",")
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1,axisbg='white')
plt.plot(bias,frequency,'-',linewidth=2)
plt.title('LC Oscillator')
plt.xlabel('Bias Voltage (V)')
plt.ylabel('Frequency GHz')
plt.savefig('LC_chars.eps',format='eps',dpi=1600)
plt.show()
#import os
#os.system("gvimdiff&")
ser.close()             # close port
