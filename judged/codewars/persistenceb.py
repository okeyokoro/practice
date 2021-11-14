def persistence(n, count=0):
    if len(str(n)) == 1 :
        return count
    else:
        j = 1
        for i in list(str(n)):
           j *= int(i)
        n =j
        count += 1
        return persistence(n, count)

# res = persistence(999)
# print res
print persistence(999)
