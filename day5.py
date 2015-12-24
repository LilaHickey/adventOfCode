import collections 
import unittest

niceList = []
naughtyList = []

contains = ['a', 'e', 'i', 'o', 'u']

doesNotContain = ['ab', 'cd', 'pq', 'xy']



def checkNaughty(input):
	print "Naughty check"
	for i in doesNotContain:
		if i in input:
			#print i
			#print input
			return False
	return True


def vowelCheck(input):
	vowelCounter = collections.Counter(contains)
	#print list(vowelCounter.elements())
	#print input
	numVowels = 0
	for i in input:
		#print i
		numVowels += vowelCounter[i]
	#print numVowels
	if numVowels>2:
		return True
	else:
		return False

def doubleCheck(input):
	#print input
	index=0
	while index<16:
		#print index
		#print input[index]
		currentChar = input[index]
		nextChar = input[index+1]
		#print currentChar, nextChar
		if currentChar == nextChar:
		#	print "MATCH!"
			return True
		index += 1
	return False
		

	

naughty = 0
f = open('input/input-day-5.txt', 'r')
lines = f.readlines()
print len(lines)
f.close()
allChecks = [checkNaughty, vowelCheck, doubleCheck]
for check  in allChecks:
	lines[:] = [x for x in lines if check(x)]	
	print len(lines)
	#lines[:] = [x for x in lines if vowelCheck(x)]
	#lines[:] = [x for x in lines if doubleCheck(x)]


#for line in lines:
	#print line
	#if checkNaughty(line):
	#	print "deleting line", line
#	else:
print type(lines)	
print len(lines)
print lines

#p.close()		
#print naughty


