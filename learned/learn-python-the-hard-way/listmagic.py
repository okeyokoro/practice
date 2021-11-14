# List Magic

#####################
# Filter
#####################
# def f(x): return x%3==0 or x%5==0
# print filter(f, range(2,25))

# def ev(i ) :return i%2 == 0
# even = filter(ev, range(1,101))
# print even

##################################
# Filter vs. List Comprehension
################################
# print [i for i in range(2,25) if i%3==0 or i%5==0]

########################
# Map
#########################
def cube(x): return x**3   # We dont need this .We should use a lamda expresion instead

print map( lambda i: i**3, range(1,11) )  # Used a lambda expression instead

# map is different from the list comprehension above *for multiple sequences
# def f(x,y): return (x,y)
# print map(f,range(1,11),range(11,21))  # This is not nested. returns it side by side. walks thru each sequence at once.

##############################
#List Comprehension vs Map
##############################

# print [(i,j) for i in range(1,11) for j in range(11,21)]  #<--- The for loops are nested *there's a j for each i
# print [( x for x in range(1,11))  for y in range(11,21)]


###########################################
# Reduce <--- works like an increment-er/or
###########################################

# def add(x,y): return x+y
# print reduce(add, range(1,11))       # A third argument could be added 
# to specify starting point e.g. print reduce(add, [], 0) ---> 0

# Useful string method -----> .strip() == .trim() in javascript
