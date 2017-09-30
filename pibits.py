
import math


# term = 0
#total = 0
#for i in range(1,MAX):
#	term = 1/(i**2)
#	total += term
#	print(math.sqrt(total) / 6)


def getTerm(i):
	return 1 / i**2

def getSum(i,REPORT=False):
	total = 0
	for i in range(1, i+1):
		total += getTerm(i)
		if(REPORT):
			print(extractPi(total))
	return total


def extractPi(aSum):
	return math.sqrt(aSum * 6.0)

assert getTerm(1) == 1
assert getTerm(2) == 1/4
assert getTerm(758) == 1/(758**2)



assert getSum(1) == 1
assert getSum(2) == 1.25

epsilon = 0.0000000001
result = getSum(25)
assert result < (1.6057234036 + epsilon)
assert result > (1.6057234036 - epsilon)

result = getSum(1000)
assert result < (1.6439345667 + epsilon)
assert result > (1.6439345667 - epsilon)

assert extractPi(6) == 6
assert extractPi(24) == 12










if(__name__=="__main__"):

	REPORT = True
	bigNumber = int(math.pow(10,9))
	getSum(bigNumber,REPORT)









	
	

