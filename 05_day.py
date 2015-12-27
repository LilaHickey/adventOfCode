import collections 
import unittest
import itertools
from itertools import tee, islice, izip

niceList = []
naughtyList = []

contains = ['a', 'e', 'i', 'o', 'u']

doesNotContain = ['ab', 'cd', 'pq', 'xy']

# borrowed from:
# http://stackoverflow.com/questions/4197805/python-for-loop-look-ahead
def get_next(some_iterable, window=1):
    items, nexts = tee(some_iterable, 2)
    nexts = islice(nexts, window, None)
    return izip(items, nexts)

def get_nextSkip(some_iterable):
    items, nexts, thirds = tee(some_iterable, 3)
    nexts = islice(nexts, 1, None)
    thirds = islice(thirds, 2, None)
    #print list(items)
    #print list(nexts)
    #print list(thirds)
    return izip(items, nexts, thirds)

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
		

def repeatCheck(input):
	#input = 'uaruacxstgmygtbaaa'
	print "input is: ", input
	patternList = []
	for char, nextChar in get_next(input):
		#print char, nextChar
		patternList.append([char, nextChar])
		#if next_line and next_line.startswith("0"):
	containsDouble = False
	for index, x in enumerate(patternList):
		#print "x", x
		for subIndex, y in enumerate(patternList):
		#	print "y", y
			if x==y:
				#print "MATCH!"
				#print "index", index
				#print "subIndex", subIndex
				if abs(index - subIndex) > 1:
					#print "TRUEMATCH", x, y, index, subIndex
					return True
	return False	

def interruptedRepeat(input):
	print input
	containsTriple = False
	for char, nextChar, thirdChar in get_nextSkip(input):
		if char == thirdChar:
			print "MATCH!"
			print char, nextChar, thirdChar
			return True
	return False


f = open('input/input-day-5.txt', 'r')
lines = f.readlines()
#lines = ['uaruacxstgmygtbaaa']
#print len(lines)
f.close()
#allChecks = [checkNaughty, vowelCheck, doubleCheck]
allChecks = [repeatCheck, interruptedRepeat]
for check  in allChecks:
	lines[:] = [x for x in lines if check(x)]	
	#print len(lines)
	#lines[:] = [x for x in lines if vowelCheck(x)]
	#lines[:] = [x for x in lines if doubleCheck(x)]


#for line in lines:
	#print line
	#if checkNaughty(line):
	#	print "deleting line", line
#	else:
print len(lines)
#print lines

#p.close()		
#print naughty


