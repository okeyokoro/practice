print "You enter a dark room with two doors.  Do you go through door #1 os door #2?"

door = raw_input(">>>")

if door == "1":
    print "There's a giant bear eating a chese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input(">>>")

    if bear == 1 or bear == 2:
        print "The bear eats your face off. Great!!"
    else:
        print "Well, doing that is probably better. Bear runs away"

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."

    insanity = raw_input(">>>")

    if insanity == "1" or insanity == "2":
        print "Your body survives, powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Great job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"         
