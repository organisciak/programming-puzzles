# This solution check for primes by dividing by previously seen primes, from lowest to
# highest
#
import math

def main():
	target = 10001 # Looking for nth prime 

	print "Prime #%d is %d" % (target, generate_primes(target)[-1])

def generate_primes(target):
	primes = [2]
	i = 1

	while len(primes) < target:
		# Skipping by two will reduce our space down by half
		i += 2 
	# Check if prime
		if isPrime(i):
			primes += [i]

	return primes

def isPrime(n):
	# One is not prime
	if n == 1:
		return False
	# All >3 primes can be written as 6k+/-1
	#
	elif n < 4:
		# Remove 2 and 3, which are dvisible by 2/3
		# But are primes
		return True
		print "test"
	# From Wikipedia article on primality testing, note
	# That all integers can be expressed as 6k+i, where
	# i is -1, 0, 1, 2, 3, or 4.
	
	# We can cover all the cases of 6k+0, 6k+2, and 6k+4
	# by testing for even numbers:
	elif n % 2 == 0:
		return False
	# And we can account for 6k+3 by checking for division by 3:
	elif n % 3 == 0:
		return False
	# Which leaves 6k+1 and 6k-1 to test as possible
	# divisors of our number
	# Remembering that at sqrt(n) divisors will simply flip, we only
	# need to check up until sqrt(n)
	lim = math.floor(math.sqrt(n))
	l = 6 # l = 6*k
	while l + 1 <= lim:
		if n % (l+1) == 0:
			return False
		l += 6
	
	l = 6
	while l - 1 <= lim:
		if n % (l-1) == 0:
			return False
		l += 6
	return True

if __name__ == '__main__':
	main()
