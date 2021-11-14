#learning to do recursion

def factorial(f):
    if f<1:  # Step 1: Define the base case
        return 1
    else:
        return  f*factorial(f-1) #Step 2: Recursive call




print "\nInput the number to find the factorial."
num = input(">>>")
print factorial(num)
