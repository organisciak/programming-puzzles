'''
Equal Partitions

From: http://programmingpraxis.com/2011/11/15/phil-harveys-puzzle/

Task: "Partition {1,...,16} into two sets of equal size so each subset has the same sum, sum of squares and sum of cubes."
'''

def calculate(partition1):
	'''
	Calculate sum, sum of squares, and sum of cubes for two partition from
	the numbers 1..16. Input a list of the first partition.
	'''
	partition2 = [i for i in range(1,17) if i not in partition1]

	sum_p1 = sum(partition1)
	sum_p2 = sum(partition2)
	sum2_p1 = sum2(partition1)
	sum2_p2 = sum2(partition2)
	sum3_p1 = sum3(partition1)
	sum3_p2 = sum3(partition2) 

	return sum_p1==sum_p2 and sum2_p1==sum2_p2 and sum3_p1==sum3_p1

def sum2(l): return sum([i**2 for i in l])
def sum3(l): return sum([i**3 for i in l])

calculate([1,2,3])

a = range(1, 17)

desired = [sum(a)/2, sum2(a)/2, sum3(a)/2]

#Calculate the effect on the sum that each number has
def difference(popper, target, attempted, banned=[(0,0)]):
	original = popper[:]
	adder = inverse(popper)
	best = 10000000
	best_combo = (0,0)
	for i,pop_num in enumerate(popper):
		for j, add_num in enumerate(adder):
			deviation = abs(target[0]-pop_num+add_num) + abs(target[1]-pop_num**2+add_num**2)**1/2 + abs(target[2]-pop_num**3+add_num**3)**1/3
			if abs(deviation) < best and (i,j) not in banned:
				best = abs(deviation)
				best_combo = (i,j)
	#Make the best replacement
	print popper, adder
	print popper[best_combo[0]], adder[best_combo[1]], attempted
	popper[best_combo[0]] = adder[best_combo[1]]
	if popper in attempted:
		print "Already attempted, trying something better"
		banned += [best_combo]
		print "Banned", banned
		return difference(original[:], target, attempted, banned)
	else:
		return popper

def inverse(l):
	return [i for i in range(1,17) if i not in l]
	
list1 = range(1,9)
i =0
attempted_lists = [list1[:]]
while i<65:
	#Calculate difference of each from the ideal values
	diffs = [sum(list1)-desired[0], sum2(list1)-desired[1], sum3(list1)-desired[2]]
	print list1, "|||", diffs
	if sum(diffs) == 0:
		print "Found it!"
		break
	list1 = difference(list1[:], diffs, attempted_lists)
	list1.sort()
	attempted_lists += [list1[:]]
	i += 1
'''			
#Since they're two sets of equal size
for i1 in a:
	for i2 in a:
		for i3 in a:
			for i4 in a:
				for i5 in a:
					for i6 in a:
						for i7 in a:
							for i8 in a:
								b=[i1,i2,i3,i4,i5,i6,i7,i8]
								if [sum(b)/2, sum2(b)/2, sum3(b)/2] == desired:
									print "Success with",", ".join(candidate)
									break
'''
