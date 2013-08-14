# Find the sum of all the primes below two million.
#

# Using the Sieve of Eratosthenes, with the following optimizations
# When the square of the sieve prime is higher than the target, assume
#   remaining numbers are primes
# Start with only odd numbers

target = 2000000 # Looking for nth prime 
possible_primes = range(3, target+1, 2)
sum_primes = 2
while True:
	if len(possible_primes) is 0:
		break
	p = possible_primes[0]
	if p*p > target:
		sum_primes += sum(possible_primes)
		break
	possible_primes = [num for num in possible_primes[1:] if num % p != 0]
	sum_primes += p
print sum_primes
