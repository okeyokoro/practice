def fib(x):
    a=0
    b=1
    while a<= x:
        print a,
        c = a+b
        a = b
        b = c
x = input("How many? ")
fib(x)
