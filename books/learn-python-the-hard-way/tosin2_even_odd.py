#This is a program to calculate the " parity " of a number...is it even or odd?
#This is the function I'm gonna be using
def even_or_odd(number):
    #I'm going to use % ("modulos") which returns the remainder after division
    if number%2 == 0:
        result = "\n%d is an even number.\n"% number
    else:
        result = "\n%d is an odd number.\n"% number

    print result


def get():
    n = input("\nInput Number >>> ")   #This "gets" the number from the user
    even_or_odd(n)          #I then have to "pass it through the function I wrote earlier"
    get()

get()
