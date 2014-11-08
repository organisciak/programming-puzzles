# Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
# a + b + c = 1000
# a + b = 1000 - sqrt(a^2 + b^2)

def main():
	n = 1000
	limit = int(n / 3)
	for a in range(1, limit + 1):
		if test(a, n = n, lim=limit):
			return

def test(a, n, lim):
	for b in range(n, 1, -1):
		c1 = math.sqrt(b*b + a*a)
		if c1 % 1 != 0:
			continue
		c2 = n - a - b
		if c1 > c2:
			continue
		elif c2 < c1:
			return False
		elif c1 == c2:
			ans = a * b * c1
			print "The answer is {}, product of {}, {}, {}".format(ans, a, b, c1)
			return True

if __name__ == '__main__':
	main()
