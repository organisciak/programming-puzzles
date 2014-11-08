def fib(x,y):
	z = x + y

n, i = 1000, 2
x, y = 1, 1

while y < pow(10, n-1):
	i += 1
	z = x + y
	x, y = y, z
print i, y
