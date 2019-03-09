"""
PYTHON NON-PRIMES GENERATOR
===========================

Given an integer k, print the first k non-prime positive integers,
each on a new line.

For example, if k = 10, the output would be:

1
4
6
8
9
10
12
14
15
16
 

Function Description 
====================
Complete the function manipulate_generator in the editor below.
The function must manipulate the generator function so that the 
first k non-prime positive integers are printed, each on a separate line.


manipulate_generator has the following parameter(s):
    g:  a generator
    n: an integer

 

Constraints
==========
1 ≤ k ≤ 105  
 

Input Format For Custom Testing
===============================

Sample Case 0
=============

Sample Input 0
==============
12

Sample Output 0
==============
1
4
6
8
9
10
12
14
15
16
18
20

Explanation 0
=============
The output contains the first 12 non-prime positive integers.
"""

def manipulate_generator(generator, n):
    """Clever Test of Coroutines and Generator expressions"""
    while True:
        n = next(generator)
        # if the next value is a prime. dont send it
        # keep going until you find a non-prime
        # then generator.send(non-prime)
        for number in range(2,n):   # test every number from 2 to n-1.
            if n % number == 0:     # if it is divisible by ANY number.
                generator.send(n-1) # send n. It is a non-prime.
                return              # stop the loop


###############################################
### From this point down is the test suite  ###
###############################################
def positive_integers_generator():
    n = 1
    while True:
        x = yield n  # this spits out the present value of n; AND waits to recieve values sent through send(<value>)
        if x is not None:  # After investigation, x IS None
            n = x
        else:
            n += 1

k = int(input())
g = positive_integers_generator()

for _ in range(k):
    n = next(g) # get value from generator --> 1
    print(n)    # print value gotten
    manipulate_generator(g, n)   # manipulate the generator so that it skips a prime number
                                 # you can  do this by calling next(g) AND .send() --> send a non-prime

