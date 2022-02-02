from tracemalloc import stop
import utilities.primeGen as primeGen
import math

num = 600851475143

possibleFactors = primeGen.genRoof(int(math.sqrt(num)))[::-1]

for i in possibleFactors:
	if num % i == 0:
		print(i)