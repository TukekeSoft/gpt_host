import numpy
from matplotlib import pyplot as plt 
data=numpy.genfromtxt('LC.csv',skiprows=1,delimiter=',')
frequency=data[:,1]
bias=data[:,0]
plt.plot(bias,frequency/1e9,'-',linewidth=2)

plt.title('LC Oscillator')
plt.xlabel('Bias Voltage (V)')
plt.ylabel(r'Frequency (GHz)')
plt.show()
plt.savefig('LC.eps',format='eps',dpi=1000)

#ser = serial.Serial('/dev/ttyACM0',4800,timeout=10)
#print ser.name
#for i in range(0,20)
#	tf = ser.read(2)
#	tb = ser.read(2)
#	f(i) = tf(0) + tf(1)*256
#	bias(i) tb(0) + tb(1)*256

#plt.plot(s,b,'-',linewidth=1)
#plt.title('LC Oscillator')
#plt.xlabel('Bias Voltage (V)')
#plt.ylabel(r'Frequency (GHz)')
