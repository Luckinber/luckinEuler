from tracemalloc import stop
from luckinUtils import primeGen
import math

def lrgPrimeFact(num):
	for i in primeGen(int(math.sqrt(num)))[::-1]:
		if num % i == 0:
			return(i)

print(lrgPrimeFact(600851475143))