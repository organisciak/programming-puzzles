# This solution check for primes by dividing by previously seen primes, from lowest to
# highest
#
target = 10001 # Looking for nth prime 
known_primes = [2]
prime_factors = []
i = 1 

while True:
	i += 2 # Skipping by two will reduce our space down by half
	# Check if prime
	for prime in known_primes:
		if i % prime == 0:
			break # This break is for the primes loop
	else:
		known_primes += [i]
		if len(known_primes) == target:
			print known_primes[-1]
			break # This break is for the While loop
