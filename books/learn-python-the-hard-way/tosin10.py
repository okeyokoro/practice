def line(x):
    for line in range(1,x+1):
        print "\n"
        for i in range(1,line+1):
            print i,

x = input("\nHow many lines do you want to print? ")
line(x)
