'''
# 99 Python Problems - Part 1: Lists #

Based on the 99 Prolog Problems
(https://sites.google.com/site/prologsite/prolog-problems).
'''

'''1.01 (*) Find the last element of a list.'''
# Sample Data
l = ['a', 'b', 'c', 'd']
# Solution
answer = l[-1]
# Test
assert answer == 'd'


'''1.02 (*) Find the last but one element of a list.'''
# Solution
answer = l[-2]
# Test
assert answer == 'c'


'''1.03 (*) Find the K'th element of a list.'''
# Sample Data
k = 3
assert k <= len(l)
# Solution
answer = l[k-1]
# Test
assert answer == 'c'


'''1.04 (*) Find the number of elements of a list.'''
# Solution
answer = len(l)
# Test
assert answer is 4


'''1.05 (*) Reverse a list.'''
#answer - l.reverse() #Reverse in place
answer = l[::-1]  # Using slices (start:stop:step)
assert answer == ['d', 'c', 'b', 'a']


'''1.06 (*) Find out whether a list is a palindrome.
A palindrome can be read forward or backward; e.g. [x, a, m, a, x].'''
# Sample Data
l2 = ['x', 'a', 'm', 'a', 'x']


# Solution
def palindrome(l):
    return l == l[::-1]
# Test
assert palindrome(l) is False and palindrome(l2) is True


'''1.07 (**) Flatten a nested list structure.
Transform a list, possibly holding lists as elements into a 'flat' list by
replacing each list with its elements (recursively).'''
# Sample data
l3 = ['a', ['b', ['c', 'd'], 'e']]


# Solution
def flatten(l):
    flat = []
    for item in l:
        if type(item) is list:
            flat += flatten(item)
        else:
            flat += item
    return flat
# Test
assert flatten(l3) == ['a', 'b', 'c', 'd', 'e']


'''1.08 (**) Eliminate consecutive duplicates of list elements.
If a list contains repeated elements they should be replaced with a single
copy of the element. The order of the elements should not be changed.

Example:
?- compress([a, a, a, a, b, c, c, a, a, d, e, e, e, e], X).
X = [a, b, c, a, d, e]'''
# Sample Data
l4 = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']


# Solution
### Make a list using only the last value of consecutive duplicates
def compress(l):
    return [item for i, item in enumerate(l)
            if i+1 == len(l) or item != l[i+1]
            ]
# Test
assert compress(l4) == ['a', 'b', 'c', 'a', 'd', 'e']


'''1.09 (**) Pack consecutive duplicates of list elements into sublists.
        If a list contains repeated elements they should be placed in separate
        sublists.

        Example:
        ?- pack([a, a, a, a, b, c, c, a, a, d, e, e, e, e], X).
        X = [[a, a, a, a],[b],[c, c],[a, a],[d],[e, e, e, e]]'''


#Solution
def pack(l):
        packed = []
        builder = []
        for item in l:
                if len(builder) > 0 and item != builder[0]:
                        packed += [builder]
                        builder = []
                builder += item
        packed += [builder]
        return packed
# Test
assert pack(l4) == [['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a'], ['d'],
                    ['e', 'e', 'e', 'e']]


'''1.10 (*) Run-length encoding of a list.
Use the result of problem 1.09 to implement the so-called run-length encoding
data compression method. Consecutive duplicates of elements are encoded as
terms [N, E] where N is the number of duplicates of the element E.'''

# Solution
encode = lambda l: [[len(a), a[0]] for a in pack(l4) if a != []]
# Test
assert encode(l4) == [[4, 'a'], [1, 'b'], [2, 'c'],
                      [2, 'a'], [1, 'd'], [4, 'e']]


'''1.11 (*) Modified run-length encoding.
Modify the result of problem 1.10 in such a way that if an element has no
duplicates it is simply copied into the result list. Only elements with
duplicates are transferred as [N, E] terms.'''
# Solution
encode_modified = lambda l: [([len(a), a[0]] if len(a) != 1 else a[0])
                             for a in pack(l4) if a != []]
# Test
assert encode_modified(l4) == [[4, 'a'], 'b', [2, 'c'],
                               [2, 'a'], 'd', [4, 'e']]


'''1.12 (**) Decode a run-length encoded list.'''
# Sample Data
l5 = encode_modified(l4)


# Solution
def decode(l):
        builder = []
        for x in l:
                if type(x) == list:
                        builder += [x[1]]*x[0]
                else:
                        builder += [x]
        return builder
# Test
assert decode(l5) == l4


'''1.13 (**) Run-length encoding of a list (direct solution).
Implement the so-called run-length encoding data compression method directly.
I.e. don't explicitly create the sublists containing the duplicates, as in
problem 1.09, but only count them. As in problem 1.11, simplify the result list
by replacing the singleton terms [1, X] by X.
        Example:
        ?- encode_direct([a, a, a, a, b, c, c, a, a, d, e, e, e, e], X).
        X = [[4, a], b,[2, c],[2, a], d,[4, e]]'''


#Solution
def encode_direct(l):
        builder = []
        count = 0
        for i, item in enumerate(l):
                count += 1
                if i+1 is len(l) or item is not l[i+1]:
                        builder += [[count, item]] if count > 1 else [item]
                        count = 0
        return builder
#Test
assert encode_direct(l4) == encode_modified(l4)

'''1.14 (*) Duplicate the elements of a list.
Example:
?- dupli([a, b, c, c, d], X).
X = [a, a, b, b, c, c, c, c, d, d]'''
# Sample Data
l5 = ['a', 'b', 'c', 'c', 'd']


# Solution
def dupli(l, times=2):
        builder = []
        for item in l:
                for i in range(times):
                        builder += [item]
        return builder
# Test
assert dupli(l5) == ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']

'''1.15 (**) Duplicate the elements of a list a given number of times.
Example:
?- dupli([a, b, c], 3, X).
X = [a, a, a, b, b, b, c, c, c]

What are the results of the goal:
?- dupli(X, 3, Y).'''
# Sample data
l6 = ['a', 'b', 'c']
# Solution above
# Test
assert dupli(l6, 3) == ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
assert dupli(dupli(l6, 3)) == ['a']*6+['b']*6+['c']*6

'''1.16 (**) Drop every N'th element from a list.
Example:
?- drop([a, b, c, d, e, f, g, h, i, k], 3, X).
X = [a, b, d, e, g, h, k]'''
# Sample data
l7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']


# Solution
def drop(l, nskip):
        return [a for i, a in enumerate(l) if (i+1) % nskip is not 0]
# Test
assert drop(l7, 3) == ['a', 'b', 'd', 'e', 'g', 'h', 'k']

'''1.17 (*) Split a list into two parts; the length of the first part is given.
Do not use any predefined predicates.

Example:
?- split([a, b, c, d, e, f, g, h, i, k], 3, L1, L2).
L1 = [a, b, c]
L2 = [d, e, f, g, h, i, k]'''


# Solution
def split(l, div):
        assert len(l) >= div
        return (l[:div], l[div:])

# Test
L1, L2 = split(l7, 3)
assert L1 == ['a', 'b', 'c']
assert L2 == ['d', 'e', 'f', 'g', 'h', 'i', 'k']

'''1.18 (**) Extract a slice from a list.
Given two indices, I and K, the slice is the list containing the elements
between the I'th and K'th element of the original list (both limits included).
Start counting the elements with 1.

Example:
?- slice([a, b, c, d, e, f, g, h, i, k], 3, 7, L).
X = [c, d, e, f, g]'''


# Solution
def slice(l, start, stop):
        return l[start-1:stop]
# Test
assert slice(l7, 3, 7) == ['c', 'd', 'e', 'f', 'g']

'''1.19 (**) Rotate a list N places to the left.
Examples:
?- rotate([a, b, c, d, e, f, g, h], 3, X).
X = [d, e, f, g, h, a, b, c]

?- rotate([a, b, c, d, e, f, g, h],-2, X).
X = [g, h, a, b, c, d, e, f]

Hint: Use the predefined predicates length/2 and append/3, as well as the
result of problem 1.17.'''

# Sample Data
l8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# Solution
def rotate(l, index):
        return l[index:]+l[:index]
# Test
assert rotate(l8, 3) == ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
assert rotate(l8, -2) == ['g', 'h', 'a', 'b', 'c', 'd', 'e', 'f']

'''1.20 (*) Remove the K'th element from a list.
Example:
?- remove_at(X,[a, b, c, d], 2, R).
X = b
R = [a, c, d]'''


# Solution
def remove_at(l, k):
        return (l[k-1], l[:k-1]+l[k:])
# Test
X, R = remove_at(l, 2)
assert X == 'b' and R == ['a', 'c', 'd']

'''1.21 (*) Insert an element at a given position into a list.
Example:
?- insert_at(alfa,[a, b, c, d], 2, L).
L = [a, alfa, b, c, d]'''


# Solution
def insert_at(l, val, index):
        return l[:index-1]+[val]+l[index-1:]
# Test
assert insert_at(l, 'alfa', 2) == ['a', 'alfa', 'b', 'c', 'd']

'''1.22 (*) Create a list containing all integers within a given range.
Example:
?- range(4, 9, L).
L = [4, 5, 6, 7, 8, 9]'''


# range is included in Python, though with a different index.
# Solution
def range2(start, end):
        ## Cheating! (Though much better performance)
        l = range(start+1, start+1)
        # Not cheating
        l = []
        while start <= end:
                l += [start]
                start += 1
        return l
# Test
assert range2(4, 9) == [4, 5, 6, 7, 8, 9]

'''1.23 (**) Extract a given number of randomly se:
?- rnd_select([a, b, c, d, e, f, g, h], 3, L).
L = [e, d, a]

Hint: Use the built-in random number generator random/2 and the result of
problem 1.20.'''
# Solution
import random


def rnd_select(l, n):
        new_l = []
        for i in range(0, n):
                index = random.randrange(len(l))
                new_l += [l[index]]
        return new_l
# Test
print "3 Random letters from a-h:", rnd_select(l8, 3)

'''1.24 (*) Lotto: Draw N different random numbers from the set 1..M.
The selected numbers shall be put into a result list.
Example:
?- rnd_select(6, 49, L).
L = [23, 1, 17, 33, 21, 37]

Hint: Combine the solutions of problems 1.22 and 1.23.'''


# Solution
def rnd_select2(N, M):
    l = range2(1, M)
    return rnd_select(l, N)
# Test
print "6 Random numbers between 6 and 49:", rnd_select2(6, 49)

'''1.25 (*) Generate a random permutation of the elements of a list.
Example:
?- rnd_permu([a, b, c, d, e, f], L).
L = [b, a, d, c, e, f]

Hint: Use the solution of problem 1.23.'''

# Sample Data
l9 = ['a', 'b', 'c', 'd', 'e', 'f']


# Solution
def rnd_permu(l):
    return rnd_select(l, len(l))

# Test
assert (l9 != rnd_permu(l9) and l9 != rnd_permu(l9)
        and len(l9) == len(rnd_permu(l9)))


'''1.26 (**) Generate the combinations of K distinct objects chosen from the N
elements of a list
In how many ways can a committee of 3 be chosen from a group of 12 people? We
all know that there are C(12, 3) = 220 possibilities (C(N, K) denotes the
well-known binomial coefficients). For pure mathematicians, this result may be
great. But we want to really generate all the possibilities (via backtracking).

Example:
?- combination(3,[a, b, c, d, e, f], L).
L = [a, b, c] ;
L = [a, b, d] ;
L = [a, b, e] ;
...
'''


# Solution
def combination(l, K):
    pass


'''1.27 (**) Group the elements of a set into disjoint subsets.
a) In how many ways can a group of 9 people work in 3 disjoint subgroups of 2,
3 and 4 persons? Write a predicate that generates all the possibilities via
backtracking.

Example:
?- group3([aldo, beat, carla, david, evi, flip, gary, hugo, ida], G1, G2, G3).
G1 = [aldo, beat], G2 = [carla, david, evi], G3 = [flip, gary, hugo, ida]
...

b) Generalize the above predicate in a way that we can specify a list of group
sizes and the predicate will return a list of groups.

Example:
?- group([aldo, beat, carla, david, evi, flip, gary, hugo, ida],[2, 2, 5], Gs).
Gs = [[aldo, beat],[carla, david],[evi, flip, gary, hugo, ida]]
...

Note that we do not want permutations of the group members; i.e. [[aldo, beat],
...] is the same solution as [[beat, aldo],...]. However, we make a difference
between [[aldo, beat],[carla, david],...] and [[carla, david],[aldo, beat],...]

You may find more about this combinatorial problem in a good book on discrete
mathematics under the term "multinomial coefficients".'''

'''1.28 (**) Sorting a list of lists according to length of sublists
a) We suppose that a list (InList) contains elements that are lists themselves.
The objective is to sort the elements of InList according to their length.
E.g. short lists first, longer lists later, or vice versa.

Example:
?- lsort([[a, b, c],[d, e],[f, g, h],[d, e],[i, j, k, l],[m, n],[o]], L).
L = [[o], [d, e], [d, e], [m, n], [a, b, c], [f, g, h], [i, j, k, l]]

b) Again, we suppose that a list (InList) contains elements that are lists
themselves. But this time the objective is to sort the elements of InList
according to their length frequency; i.e. in the default, where sorting is done
ascendingly, lists with rare lengths are placed first, others with a more
frequent length come later.

Example:
?- lfsort([[a, b, c],[d, e],[f, g, h],[d, e],[i, j, k, l],[m, n],[o]], L).
L = [[i, j, k, l], [o], [a, b, c], [f, g, h], [d, e], [d, e], [m, n]]

Note that in the above example, the first two lists in the result L have length
4 and 1, both lengths appear just once. The third and forth list have length 3;
there are two list of this length. And finally, the last three lists have
length 2. This is the most frequent length.
'''
