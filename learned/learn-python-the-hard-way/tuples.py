# Tuples & Sets
#############################
tup = [1,2,3],[4,7,5,6]
print tup

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

fruit = set(basket)               # create a set without duplicates
fruit

set(['orange', 'pear', 'apple', 'banana'])

if 'orange' in fruit :                # fast membership testing
    print True
print 'crabgrass' in fruit


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print a                                  # unique letters in a

print a - b                              # letters in a but not in b

print a | b                              # letters in either a or b

print a & b                              # letters in both a and b ===> INTERSECTION

print a ^ b                              # letters in a or b but not both ====> COMLEMENT OF INTERSECTION 

###########################
#Set Comprehension
###########################
a = set( x for x in "abracadabra" if x not in "abc")
print a
