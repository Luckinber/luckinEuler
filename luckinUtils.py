def primeGen(roof):
	# Construct array
	primesIndex = [1]*roof
	primes = []

	# 1 and 0 are default booted
	primesIndex[0] = 0
	primesIndex[1] = 0

	# Iterate through the index of primes up to root of roof
	for i in range(len(primesIndex)):
		if primesIndex[i] == 1 and i*i <= roof:
			# Scratch multiples of said value up to roof
			j = i*2
			while j < roof:
				primesIndex[j] = 0
				j += i
	
	for i in range(len(primesIndex)):
		if primesIndex[i] == 1:
			primes.append(i)
	return(primes)

