import itertools
from operator import mul, add

def calculateWrappingPaper(object):
	size = 0
	smallestSide=10000000000
	print object
	objectMatrix = itertools.combinations(object, 2)
	for p in objectMatrix:
		print p
		#print p[0]
		#print type(p)
		#print type(p[0])
		#intP = [map(int, x) for x in p]
		#print intP
		result = reduce(mul,p)
		if result<smallestSide:
			smallestSide = result
		size += result
	size = 2*size
	size = size + smallestSide
	print size
	return size

def calculateRibbon(object):
	size = 0
	bow = 0
	print object
	print type(object)
	bow = reduce(mul,object)
	print bow
	object.remove(max(i for i in object))
	print object
	size = sum(object)
	size = size*2
	size = size + bow
	print size
	return size
	
			




totalSize = totalRibbon = 0
f = open('input/input-day-2.txt', 'r')
for line in f:
	#print type(line)
	line = line.strip()
	#print type(line)
	line = line.split("x")
	line = [int(x) for x in line]
	totalSize = totalSize + calculateWrappingPaper(line)
	totalRibbon = totalRibbon + calculateRibbon(line)
print totalSize
print totalRibbon
f.close()