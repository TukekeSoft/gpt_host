import serial
import array
import binascii
import numpy
ser = serial.Serial('/dev/ttyACM0', 4800,timeout=10)  # open first serial port
print ser.name          				# check which port was really used
print("Hit Enter to ping device...")
raw_input()
ser.write('a');
print("Hit enter to load device with test data...");
raw_input();
s=[]
test_data = ("1234ABCDEFGHIJKLMNOP")
ser.write(test_data)      # write a string
test_data = list(test_data)
s1=[]
for i in range(0,20):
	s.append(ord(ser.read()))

for i in range(0,20):
	s1.append(ord(ser.read()))


result = []
result1= []
source = []
for i in range(0,20):   
    for j in range(0,7):
		result.append(str(((s[i] >> j) & 1)));
		result.append('\n')

result =''.join(result)

for i in range(0,20):   
    for j in range(0,7):
		result1.append(str(((s1[i] >> j) & 1)));
		result1.append('\n')

result1 =''.join(result1)


for i in range(0,20):   
    for j in range(0,7):
		source.append(str(((ord(test_data[i]) >> j) & 1)));
		source.append('\n')

source =''.join(source)

#print result

ser.close()             # close port

text_file = open("Output1.txt", "w")
text_file.write(source)
text_file.close()
text_file = open("Output2.txt", "w")
text_file.write(result)
text_file.close()
text_file = open("Output3.txt", "w")
text_file.write(result1)
text_file.close()
import os
os.system("gvimdiff Output1.txt Output2.txt Output3.txt&")






