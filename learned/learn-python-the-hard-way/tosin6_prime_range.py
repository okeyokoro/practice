import math

def prime(x):
    if x > 100 :
        p1 = [x%i == 0 for i in range(2,int(math.ceil(x**0.5)))]
        return 0 if p1.count(True) >= 1 else x
    else:
        p2 = [x%i == 0 for i in range(2,x)]
        return 0 if p2.count(True) >= 1 else x

def prime_test(n):
    primes = [prime(i) for i in range(2, n)]
    print sorted(primes)[primes.count(0):]

up = input("Input Range >>>")

prime_test(up)
