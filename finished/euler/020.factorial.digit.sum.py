factorial = lambda x: reduce(lambda y, z: y * z, range(1, x + 1))
sumdigits = lambda x: reduce(lambda y, z: y + int(z), list(str(x)), 0)

n = 100
a = factorial(n)
b = sumdigits(a)
print a, b
