# Recursive program to calculate prime number

def prime(n, t=1):
    #base code
    if n<=1 :
        print "\nNot a prime number.\n"
    else:
        # If it greater than 1...
        d = n-t  # This variable stores all the numbers less than n

        if n%d == 0 and d != 1: # If n can be divided by a number after it and that number is greater than 1. it is not  a prime
            print "\n%d is not a prime number.\n"% n
        elif d == 1 :
            print "\n%d is a prime number.\n"% n
        else:      # If it cant be divided by the number after it
            t+=1   # decrease d to the next number
            prime(n, t)


number = input("\nInput >>> ")
prime(number)
