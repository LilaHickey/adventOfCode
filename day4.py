import md5

key='yzbqklnj'
adventCoins = []

def findAdventCoin(secretKey, currentNumber):
	#print "logging"
	candidateValue = secretKey+str(currentNumber)
	#print candidateValue
	candidateCoin = md5.new(candidateValue).hexdigest()	
	#candidateCoin = '000001dbbfa3a5c83a2d506429c7b00e'
	#print candidateCoin
	if candidateCoin[0:6]=='000000':
		#print "it's a match!"
		print candidateValue
		adventCoins.append(candidateCoin)

i=0
while len(adventCoins)<1:
	findAdventCoin(key, i)
	i+=1

#print adventCoins



