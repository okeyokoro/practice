# %d is for digits/numbers
x= "There are %d types of people."%10
binary = "binary"
do_not = "don't"
# %s is for strings
y = "Those who know %s and those who %s"%(binary, do_not)

print x
print y
# %r is basically for anything; if it is a string it will appear with "" beause it displays raw data
# %r is best for debugging apparently
# some chaining going on here
print "I said: %r"% x
print "I also said '%s'."% y
# boolean
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# so you could do things this way too, break it up instead of doing it all at once
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
