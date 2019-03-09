def loop(i):

    while i<6:
        print "At the top i is %d"% i
        numbers.append(i)
        i +=2
        print "Numbers now: ", numbers
        print "At the bottom i is %d"% i

def loop2():

    for i in range(6):
        print "At the top i is %d"% int(i)
        numbers.append(int(i))
        print "Numbers now: ", numbers
        print "At the bottom i is %d"% (int(i)+1)

i = 0
numbers = []
loop2()

print "The numbers: "

for num in numbers:
    print num
