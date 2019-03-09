def upside(row):
    for i in range(row,0,-1):
        for j in range(row-i):
            print " " ,
        for j in range((i*2)-1):
            print "*",
        print 

x = input("\nHow many lines? ")
if x >0:
    upside(x)
else:
    print """I need a positive integer to do this.\nWhy do you have to be "that" guy?"""
