
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

