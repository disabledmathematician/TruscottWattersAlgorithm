"""
['1', '10', '100', '1000', '10000', '100000', '1000000', '10000000', '100000000', '1000000000', '10000000000', '100000000000', '1000000000000', '10000000000000', '100000000000000', '1000000000000000', '10000000000000000']
['1', '10', '100', '1000', '10000', '100000', '1000000', '10000000', '100000000', '1000000000', '10000000000', '100000000000', '1000000000000', '10000000000000', '100000000000000', '1000000000000000', '10000000000000000', '100000000000000000']
['1', '10', '100', '1000', '10000', '100000', '1000000', '10000000', '100000000', '1000000000', '10000000000', '100000000000', '1000000000000', '10000000000000', '100000000000000', '1000000000000000', '10000000000000000', '100000000000000000']
Charles Truscott Watters
Trying divide and conquer trees
I love you Tai, I love you Mark

[Program finished]
""" 

def Charles():
	s = 2 ** 18 + 1
	rep = ""
	res = ""
	n = 0
	while n <= 17:
#		print(str(bin(2 **n)[2:]))
#		print(",")
		rep += str(bin(2 ** n)[2:])
		if n <= 17:
			rep += ","
		n += 1
	n = 0
	while n <= 18 ** 2:
		res += rep
		n += 18
#	while n <= 18:
#		print(str(bin(s)))
#		rep += str(bin(s))
#		res += str(bin(s))
#		s >>= 1
#		n += 1
#	print("Initial: {}".format(rep))
#	print("Consequentual: {}".format(res))
	res = res.split(",")
	print(res[0:17])
	print(res[18: 2 * 18])
	print(res[2 * 18: 3 * 18])
	print("Charles Truscott Watters")
	print("Trying divide and conquer trees")
	print("I love you Tai, I love you Mark")

Charles()