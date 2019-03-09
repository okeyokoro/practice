
# this one is like the previous scripts using argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg: %r"% (arg1, arg2)

# apparently that "*args" is actually an unpoular way of passing arguments, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r"% (arg1, arg2)

#this takes just one argument
def print_one(arg1):
    print "arg1: %r"% arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
