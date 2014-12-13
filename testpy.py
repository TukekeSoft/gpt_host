def s_to_bitlist(s):
	ords = (ord(c) for c in s)
	shifts = (7, 6, 5, 4, 3, 2, 1, 0)
	return [(o >> shift) & 1 for o in ords for shift in shifts]

import bitarray
ba=bitarray.bitarray()
ba
s=ba.fromstring('Ha')
print(s)

x=s_to_bitlist('0')
print(x[4])

