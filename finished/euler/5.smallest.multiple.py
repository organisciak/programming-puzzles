# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
	print brute(range(1, 20+1))

# Approach 1: Brute force, incrementing up
# Range argument is a list of all the values that n needs to be divisible by
def brute(nums):

	# Simplify the number range by removing lower multiples
	for n in nums[::-1]:
		nums = [m for m in nums if n % m != 0 or m is n]

	# We only need to by the product of the lowest and highest of the remaining nums
	step = max(nums) * min(nums)

	i = 0
	while True:
		i += step
		if sum([i % j for j in nums]) is 0:
			break
	return i
	


if __name__ == '__main__':
	main()
