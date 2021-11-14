def tower(n):
    A = [i for i in range(1, n + 1)]
    B = []
    C = []
    count = 0
    t = 2**len(A+B+C)

    while count < t:
        x = [A, B, C]
        b = sorted(x)
        # we wanna see what's happening at every stage
        print "\n", x, "\r\t\t\t\t\t\t\t\t\tStep: %10d\tEnd: %10d"% (count, t-1),'\n', A, B, C

        # base case <--- this will stop this madness
        if len(A) == len(B) == 0:
            return "\ndone\n"
            break

        # odd number of discs
        elif len(A + B + C) % 2 == 1:
            if count in range(0, t-1, 6):
                C.insert(0, A.pop(0))
                count += 1
                continue
            elif count in range(2, t-1, 6):
                B.insert(0, C.pop(0))
                count += 1
                continue
            elif count in range(4, t-1, 6):
                A.insert(0, B.pop(0))
                count += 1
                continue
            elif len(b[0]) == 0:
                b[0].insert(0, b[-1].pop(0))
                count += 1
                continue
            else:
                b[-1].insert(0, b[1].pop(0))
                count += 1
                continue

        # even number of discs
        else:
            if count in range(0, t-1, 6):
                B.insert(0, A.pop(0))
                count += 1
                continue
            elif count in range(2, t-1, 6):
                C.insert(0, B.pop(0))
                count += 1
                continue
            elif count in range(4, t-1, 6):
                A.insert(0, C.pop(0))
                count += 1
                continue
            elif len(b[0]) == 0:
                b[0].insert(0, b[-1].pop(0))
                count += 1
                continue
            else:
                b[-1].insert(0, b[1].pop(0))
                count += 1
                continue





x = int(input("""\n\rWe are going to play a game called "The Tower of Hanoi" \n\n\rInput an integer x (x>0)\n\n\r>>>"""))
if x>0:
    print tower(x)
else:
    print "\n\t\tInvalid Input\n\t\tTry again.\n"
