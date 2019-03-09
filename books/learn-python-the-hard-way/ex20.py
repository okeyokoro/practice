from sys import argv

# pass a file name 'test.txt' as an argument in the shell commmand
script, input_file = argv

def print_all(f):
    print f.read()#prints the entire file

def rewind(f):
    f.seek(0) #returns the pointer on the file to 0; the beginning.

def print_a_line(line_count, f):
    #readline reads line by line. It picks up from where it left off.
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kinda like a tape."

#returns the pointer on the file to 0; the beginning.
rewind(current_file) 

print "Let's print tree lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
