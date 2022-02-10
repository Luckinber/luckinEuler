from luckinUtils import primeGen

def smallestDivis(roof):
	result = 1
	for prime in primeGen(roof):
		while prime * prime <= roof:
			prime *= prime
		result *= prime		
	return result
	
print(smallestDivis(20))