def multiples(factors, roof):
	mults = []
	for i in factors:
		step = i
		while step < roof:
			if step not in mults:
				mults.append(step)
			step += i
	return(mults)

def sumMultiples(factors, roof):
	total = 0
	for i in multiples(factors, roof):
		total += i
	return(total)

print(sumMultiples([3, 5], 1000))