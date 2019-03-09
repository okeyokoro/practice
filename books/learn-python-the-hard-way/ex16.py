from sys import argv

script, filename = argv

print "We're going to erase %r"% filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit ENTER."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # this opens the file in write mode.
                             # this actually empties out the file so you can write stuff to it

#print "Truncating the file. Goodbye!"  #apparently I dont have to do this
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n"% (line1, line2, line3))


print "And finallly, we close it."
target.close()
