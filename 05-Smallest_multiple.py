from luckinUtils import primeGen	
import time	

def smallestDivis(roof):
	result = 1
	for prime in primeGen(roof):
		while prime * prime <= roof:
			prime *= prime
		result *= prime		
	return result

start = time.time()
print(smallestDivis(20))
print("Exec time is", '{:f}'.format(time.time()-start), "seconds")