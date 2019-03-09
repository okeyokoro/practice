from sys import argv

script, user_name, nick_name = argv
prompt = ">>>"

print "Hi %s, I'm the %s script."% (user_name, script)
print "I hope you don't mind me calling you %s"% nick_name
print "I'd like to ask you a few questions."
print "Do you like me %s?"% nick_name
likes = raw_input(prompt)

print "Where do you live %s?"% nick_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %s. Not sure where that is.
And you have a %r computer. Nice.
"""% (likes, lives, computer)
