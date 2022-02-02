roof = 1000
floor = 0
step = 0
mult1 = 3
mult2 = 5
total = 0

while step <= 1000:
	print("Step is", step)
	print("Total is", total)
	if step % mult1 == 0 and step % mult2 == 0:
		total += step
	elif step % mult1 == 0:
		total += step
	elif step % mult2 == 0:
		total += step
	step += 1