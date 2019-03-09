# This is program to list the even numbers between x and y
def num(i):
    if i%2 == 0 :
        return i
    else:
        return 0

def list_even(x,y):
    l = [ num(i) for i in range(x,y)]
    print sorted(l)[len(l)/2:]

print "\nThis a program to return a list of even numbers between x and y"
x=input("\nInput x:")
y=input("\nInput y:")
list_even(x,y)
