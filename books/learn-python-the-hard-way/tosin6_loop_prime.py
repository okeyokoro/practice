# Determine if number is a prime number
import math
def prime(x):
    if x > 20 :
        p1 = [x%i == 0 for i in range(2,int(math.ceil(x**0.5)))]
        print  "Not a prime" if p1.count(True) >= 1 else "That's a prime"
    elif x == 1:
        print  "Not a prime"
    else:
        p2 = [x%i == 0 for i in range(2,x)]
        print  "Not a prime" if p2.count(True) >= 1 else "That's a prime"

def get():
    n = input("\nInput Number >>> ")
    prime(n)
    get()

get()    
