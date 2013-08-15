# Which starting number, under one million, produces the longes chain?
import itertools

# Strategy: go through candidates 1..10^5 from highest down, removing candidates
# as they are encountered.

def main():
	# SLOW FOR LARGE VALUES
	top_down(1000000) # A top down approach that eliminates candidates
	
	# DOESN'T WORK:
	# reverse_collatz(1000) # An approach that starts from zero and tries to go for odd numbers

	# 

def top_down(n):
	num_tests = 0 # For stats
	longest_seq = (0, 0)
	candidates = range(2, n)

	# First run a reverse tree that favours odd numbers. Use the numbers
	# generated to remove all increments of 2 over them from the list of
	# candidates
	print len(candidates)

	# Easy collatz numbers, to filter their multiples of 2
	#easy = reverse_collatz(n)
	#print easy
	heldout = [] # Numbers that have already been removed from the candidates
	new = [2] # Numbers to test against the candidates
	tested = []
	while len(candidates) > 200000:
		# Remove all multiples of easy+2^n
		for low in new:
			candidates = list(itertools.ifilter(
				lambda x: x % int(low) != 0, candidates))
		print len(list(candidates))
		tested += new
		#new = [(n-1)/3 for n in (new+heldout) if (n-1)%3 == 0]
		temp = new + heldout
		new = map(lambda x: float(x-1)/3, temp)
		new = filter(lambda x: x % 1 == 0 and x > 1 and x % 2 != 0, new)
		heldout = map(lambda x: x*2, temp) 
		heldout = [n for n in heldout if n not in tested]
	print "Candidates whittled down to", len(candidates), "Testing downwards now"

	while len(candidates) > 0:
		num_tests += 1
		x = candidates[-1]
		seq = collatz_seq(x)
		if len(seq) > longest_seq[1]:
			longest_seq = (x, len(seq))
			print "new longest sequence: %d is %d long" % longest_seq
		candidates = [c for c in candidates if c not in seq]
		if num_tests % 10 == 0:
			print "Testing", x, "|Length=", len(candidates)
	print "Longest seq is %d, with a chain that is %d" % longest_seq


def reverse_collatz_tree(lim):
	ends = [] # list of (value, ) tuples

def reverse_collatz(lim):
	seq = [1, 2, 4, 8]
	while seq[-1] < (lim*3-1):
		if (seq[-1]-1) % 3 == 0:
			seq += [(seq[-1] - 1) / 3]
		else:
			seq += [seq[-1]*2]
	#print seq
	#print max([x for x in seq if x < lim])
	return seq

def next_collatz(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3 * n + 1


def collatz_seq(start):
	n = start
	seq = [n]
	while n != 1:
		n = next_collatz(n)
		seq += [n]
	return seq


if __name__ == '__main__':
	main()
