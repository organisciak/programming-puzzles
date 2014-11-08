# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
import time

f = open('013.large.sum.data', 'r+')
a = [int(n) for n in f.readlines()]

# Easy way: sum everything
start = time.time()
b = sum(a)
print "First 10 digits of sum are", str(b)[0:10]
end = time.time()
print "Time elapsed for simple method:", end - start
