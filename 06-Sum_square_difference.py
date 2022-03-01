def sumSquares(roof):
	total = 0
	for i in range(1, roof + 1):
		total += i*i
	return total

def squareSum(roof):
	total = 0
	for i in range(1, roof + 1):
		total += i
	return total*total

print(squareSum(100)-sumSquares(100))