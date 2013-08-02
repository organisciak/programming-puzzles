fib = [1, 2]
while True:
	new = sum(fib[-2:])
	if new > 4000000:
		break	
	else:
		fib += [new]

print sum([n for n in fib if n % 2 == 0])
