def tower(n):
    def hanoi(A = [ i for i in range(1,n+1) ], B = [], C = [], count=0):
        x  = [A,B,C]
        b = sorted(x)
        t = 2**len(A+B+C)


        # we wanna see what's happening at every stage
        print "\n", x, "\r\t\t\t\t\t\tStep: %10d\tEnd: %10d"% (count, t-1)

        # base case <--- this will stop this madness
        if len(A)==len(B)==0: return "\ndone\n"

        # odd number of discs
        elif len(A+B+C)%2 ==1:
            if count in range(0,t-1,6): C.insert(0, A.pop(0))
            elif count in range(2,t-1,6): B.insert(0, C.pop(0))
            elif count in range(4,t-1,6): A.insert(0, B.pop(0))
            elif len(b[0]) == 0 : b[0].insert(0, b[-1].pop(0))
            else: b[-1].insert(0, b[1].pop(0))

        # even number of discs
        else:
            if count in range(0,t-1,6): B.insert(0, A.pop(0))
            elif count in range(2,t-1,6): C.insert(0, B.pop(0))
            elif count in range(4,t-1,6): A.insert(0, C.pop(0))
            elif len(b[0]) == 0 : b[0].insert(0, b[-1].pop(0))
            else: b[-1].insert(0, b[1].pop(0))

        count +=1
        return hanoi(A,B,C,count)
    return hanoi()

print tower(10)
