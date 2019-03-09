# Fibbanaci series

def fib(x, a=0, b=1, count=2):

    if count>(x):
        print "end"

    else:
        c = a+b
        print c
        a = b
        b = c
        count +=1
        fib(x, a, b, count)

num = input("\nHow many elements in the Series would you like to print?  ")

print 1
fib(num)
