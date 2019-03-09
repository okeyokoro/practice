def persistence(n, count=0):
    if len(str(n)) == 1 :
        print count
    else:
        j = 1
        for i in list(str(n)):
           j *= int(i)
        n =j
        count += 1
        persistence(n, count)

persistence(3)
