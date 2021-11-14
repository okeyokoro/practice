def iq_test(numbers):
    eri = []
    num = numbers.split(" ")
    count = 0
    for i in range(len(num)) :
        eri.append(int(num[i])%2)
        count += eri[i]

    if count == 1:
        for i in range(len(num)) :
            if eri[i] == 1:
                print i+1
            else:
                continue
    else:
        for i in range(len(num)) :
            if eri[i] == 0:
                print i+1
            else:
                continue

iq_test("1 2 2")
