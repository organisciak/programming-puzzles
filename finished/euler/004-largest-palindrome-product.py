#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import time

def isPalindrome(n):
	s = str(n)
	return s == s[::-1]

def main():
	digits = 3 
	#print better(digits)
	time_methods()

def time_methods():
	for digit in range(2, 6):
		start= time.time()
		a = brute(digit)
		end = time.time()
		t = (end-start)
		print "Bruteforce of {} digits took {}s (ans: {})".format(
				digit, t, a)
		start= time.time()
		a = better(digit)
		end = time.time()
		t2 = end - start
		print "Better approach w/ {} digits took {}s (ans: {}, x{})".format(
				digit, t2, a, t/t2)

# Attempt 1: Brute Force
def brute(digits):
	lim = pow(10, digits) - 1
	palindromes = [(i*j, i, j) for (i) in range(lim, 0, -1) for j in range(lim, 0, -1)
		if isPalindrome(i*j)]
	return max(palindromes)[0]

# Alternate: Improved efficiency
def better(digits):
	lim = pow(10, digits) - 1
	largest = 0
	lower_limit = 0
	for i in range(lim, 0, -1):
		if i < lower_limit:
			return largest
		largest = compare(i, lim, largest)
		lower_limit = largest / lim

# Look at all values that multiple with i from 1:lim, finding the highest
# highest palindrome. Breaks out of loop with first palindrome, since we're
# iterating from high to low
def compare(i, lim, largest):
	for j in range(lim, 0, -1):
		k = i*j
		if isPalindrome(k) and k > largest:
			largest = k
			return largest
	return largest


if __name__ == '__main__':
	main()
