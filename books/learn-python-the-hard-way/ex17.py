from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %d to %s"% (19, to_file)

indata = open(from_file).read()
#indata = in_file.read() #apparently didnt need this Zed is tricky

print "The input file is %d bytes long"% len(indata)

print "Does the output file exist? %r"% exists(to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort."
raw_input(">>>")

out_file = open(to_file, 'w').write(indata)

print "Alright, all done."

#out_file.close()
#indata.close()
