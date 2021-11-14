def iq_test(numbers):
    eri = [ int(i)%2 for i in numbers.split(" ")]

    print eri.index(1) +1 if eri.count(1) == 1 else eri.index(0)+1

iq_test("1 2 2")
