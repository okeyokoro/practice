def solution(N):
    a = bin(N)[2:].split("1")
    hold = []
    for n in range(0,len(a)-1):
        hold.append(a[n].count("0"))
    print(sorted(hold)[len(hold)-1])

x = input(">>>")
solution(x)
