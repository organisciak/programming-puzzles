# This solution check for primes by dividing by previously seen primes, from lowest to
# highest
#
from ...lib.generatePrimes import generatePrimes

def main():
	target = 10001 # Looking for nth prime 

	print("Prime #%d is %d" % (target, generate_primes(target)[-1]))

if __name__ == '__main__':
	main()
