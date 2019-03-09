def tri(x):
    for i in range(1,x+1):
        for j in range(i):
            print "* ",
        print
x = input("\nHow many lines? ")
if x >0:
    tri(x)
else:
    print """I need a positive integer to do this.\nWhy do you have to be "that" guy?"""    
