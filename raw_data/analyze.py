import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

def graph():
	bias,frequency = np.loadtxt('LC.csv',delimiter=',',unpack=True)
	
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1,axisbg='white')
	plt.plot(x=bias,y=frequency,fat='-')
	plt.title('LC Oscilator')
	plt.ylabel('Frequency')
	plt.xlabel('Bias Voltage')
	plt.show();

graph()

#def getColumn(filename, column):
#    results = csv.reader(open(filename), delimiter=" ")
#    return [result[column] for result in results]
#
#def read_datafile(file_name):
    # the skiprows keyword is for heading, but I don't know if trailing lines
    # can be specified
#    data = np.loadtxt(file_name, delimiter=',', skiprows=1)
#    return data
#
#bias = getColumn("LC",0)
#frequency = getColumn('./LC.csv',1)
#plt.figure("Time/Volt")
#plt.xlabel("Time(ms)")
#plt.ylabel("Volt(mV)")
#plt.plot(time,volt)

#plt.show()

#x = ???
#y = ???

#fig = plt.figure()

#ax1 = fig.add_subplot(111)

#ax1.set_title("Mains power stability")    
#ax1.set_xlabel('time')
#ax1.set_ylabel('Mains voltage')

#ax1.plot(x,y, c='r', label='the data')

#leg = ax1.legend()

#plt.show()
