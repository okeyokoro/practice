print "I am 6'2\" tall." # escape dounble-quote
print 'I am 6\'2" tall.' # escape single-quotes

tabby_cat = "\tI'm tabbed in." # does tab
persian_cat = "I'm split \non a line."# new line
backslash_cat = "I'm \\ a \\ cat." # you can't just type in a backslash. you have to backslash in a bakslash.

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#I'm trying out some other escape sequences
print "This is an\a ASCII bell in action" #ASCII bell
print "This a a\bbackspace" #ASCII backspace. the the second a is removed
print "This is a\fformfeed"
print "This is\vvertical tab"
print "This is\rCarriage Return"#It wipes out everythig before it

#getting to the interesting stuff

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r"% i,
