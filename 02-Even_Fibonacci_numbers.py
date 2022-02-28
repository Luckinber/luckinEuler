def fibSeq(dig1, dig2, roof):
	fib = [dig1, dig2]
	while fib[-1] <= roof:
		fib.append(fib[-1] + fib[-2])
	return fib

def fibSum(dig1, dig2, roof):
	total = 0
	for i in fibSeq(dig1, dig2, roof):
		if i % 2 == 0:
			total += i
	return total

print(fibSum(1, 2, 4000000))