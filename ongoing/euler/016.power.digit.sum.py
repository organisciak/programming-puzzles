# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000

n = 1000
a = pow(2, n)
a = [int(n) for n in list(str(a))]
print sum(a)
