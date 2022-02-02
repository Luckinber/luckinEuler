def isPalindrome(num):
	return str(num) == str(num)[::-1]

def largest(floor, roof):
	largestProduct = 0
	for fact1 in range(roof, floor, -1):
		for fact2 in range(roof, floor, -1):
			if isPalindrome(fact1*fact2):
				if fact1 * fact2 > largestProduct:
					largestProduct = fact1 * fact2			
	return largestProduct

print(largest(0, 999))
