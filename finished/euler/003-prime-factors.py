x = 600851475143
known_primes = []
prime_factors = []
i = 1 

while True:
	i += 1
	# Check if prime
	isPrime = reduce(lambda x, y: x and (i % y != 0), known_primes, True)
	if not isPrime:
		continue
	known_primes += [i]
	# See if our value if divisible by the prime
	while (x % i == 0): 
		prime_factors += [i]
		x = x / i
	
	if x == 1:
		break
	
print prime_factors
print max(prime_factors)
