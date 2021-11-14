# Multiplication Table
def mult(x):
    for line in range(1,x+1):   # The first column
        print '\n'
        for num in range(1,x+1):
            print "%5d"%(line*num),

x = input("\nHow many lines do you want to print? ")
mult(x)
