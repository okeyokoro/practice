# ***** Glothons From Planet Percal *******
from sys import exit
from random import randint

class Scene(object): # Super Class
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object): # Super Class
    def __init__(self, scene_map): # Engine has-a attribute scene_map which is set by the user
        self.scene_map = scene_map

    def play(self): # Engine has-a function play. In this function we declare two variables: "current_scene" and "last_scene"
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene: # while the game is not over....
            next_scene_name = current_scene.enter() # the variable "next_scene_name" is set to "current_scene"(the previously declared variable) ".enter()"
            current_scene = self.scene_map.next_scene(next_scene_name) # we reset the variable "current_scene" to "next_scene" as the player has advanced
        # Gotta print out the last scene
        current_scene.enter()  # the .enter() function defined under Scene

class Death(Scene):
    quips = ["\tYou died.\n\tYou knda suck at this.",
    "\tYour mother would be proud...if you were smarter.",
    "\tI have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Central_corridor(Scene):
    def enter(self):
        print """
                 The Gothons of Planet Percal #25 have invaded your ship and destroyed
                 your entire crew. You are the last surviving member and your last
                 mission is to get the neutron destruct bomb from the Weapons Armory,
                 put it in the bridge, and blow the ship up after getting into an
                 escape pod.
                 \n
                 You're running down the central corridor to the Weapons Armory when
                 a Gothon jumps out, red scaly skin, dark grimy teeth, and evil costume
                 flowing around his hate filled body. He's blocking the door to the
                 Armory and about to pull a weapon to blast you."""

        action = raw_input(">>>")

        if action == "shoot":
            print """
                     Quick on the draw you yank out your blaster and fire it at the Gothon.
                     His clown costume is flowing and moving around his body, which throws
                     off your aim.  Your laser hits his costume but misses him entirely. This
                     completely ruins his brand new costume his mother bought him, which
                     makes him fly into an insane rage and blast you repeatedly in the face until
                     you die.
                     Then he eats you."""
            return "death"
        elif action == "dodge!":
            print """
                     Like a world class boxer you dodge, weave, slip and slide right
                     as the Gothon's blaster cranks a laser past your head.
                     In the middle of your artful dodge your foot slips and you
                     bang your head on the metal wall and pass out.
                     You wake up shortly after only to die as the Gothon stomps
                     your head and eats you."""
            return 'death'
        elif action == "tell a joke":
            print """
                     Lucky for you, they made you learn Gothon insults in the academy
                     You tell the one Gothon joke you know:
                     Lhbhe njvnfj fjvrjdco wjwjc, uiwidns jfb ejf winc, jhfin nvurrj.
                     The Gothon stops, tries not to laugh, then busts out laughing and can't move
                     While he's laughing you run up ad shoot him square in the head
                     putting him down, then jump through the Weapon Armory door."""
            return 'laser_weapon_armory'
        else:
            print 'DOES NOT COMPUTE!'
            return 'Central_corridor'

class Laser_weapon_armory(Scene):
    def enter(self):
        print """
                 You do a dive roll into the Weapon Armory, crouch and scan the room
                 for more Gothons that might be hiding. It's dead quiet, too quiet.
                 You stand up and run to the far side of the room and find the
                 neutron bomb in its container. There's a keypad lock on the box
                 and you need the code to get the bomb out. If you get the code
                 wrong 10 times then the lock closes forever and you can't
                 get the bomb. The code is 3 digits."""

        code = "%d%d%d"% (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]>>>")
        guesses = 0

        while guess != code and guesses<10:
            print 'BZZZZEDDD'
            guesses +=1
            guess = raw_input("[keypad]>>>")

        if guess == code:
            print """
                     The container clicks open and the seal breaks, letting gas out.
                     You grab the neutron bomb and run as fast as you can to the
                     bridge where you must place it in the right spot."""
            return 'the_bridge'
        else:
            print """
                     The lock uzzes one last time and then you hear a sickening
                     melting sound as the mechanism is fused together.
                     You decide to sit there, an finally the Gothons blow up the
                     ship from their ship and you die."""
            return 'death'

class The_bridge(Scene):
    def enter(self):
        print """
                 You burst onto the Bridge with the neutron destruct bomb
                 under your arm and surprise 5 Gothons who are trying to
                 take control of the ship. Each of them has an even uglier
                 clown costume than the last. They haven't pulled their
                 weapons out yet, as they see the active bomb under your
                 arm and don't want to set it off."""

        action = raw_input(">>>")

        if action == "throw the bomb":
            print """
                     In a print you throw the bomb at the group of Gothons
                     and make a leap for the door. Right as you drop it a
                     Gothon shoots you right in the back killing you.
                     As you die you see another Gothon frantically try to disarm
                     the bomb. You die knowing they will probably blow up when
                     it goes off."""
            return 'death'
        elif action == "slowly place the bomb":
            print """
                     You point your blaster at the bomb under your arm
                     and the Gothons put their hands up and start to sweat.
                     You inch backward to the door, open it, and then carefully
                     place the bomb on the floor, pointing your blaster at it.
                     You then jump back through the door, punch the close button
                     and blast the lock so the Gothons can't get out.
                     Now that the bomb is placed you run to the escape pod to
                     get off this tin can."""
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE"
            return "the_bridge"


class Escape_pod(Scene):
    def enter(self):
        print """
                 You rush through the ship desperately trying to make it to
                 the escape pod before the whole ship explodes.  It seems like
                 hardly any Gothons are on the ship, so your run is clear of
                 interference.  You get to the chamber with the escape pods, and
                 now need to pick one to take.  Some of them could be damaged
                 but you don't have time to look.  There's 5 pods, which one
                 do you take?"""

        good_pod = randint(1,5)
        guess = raw_input("[pod #]>>>")

        if int(guess) != good_pod:
            print """
                     You jump into pod %s and hit the eject button.
                     The pod escapes out into the void of space, then
                     implodes as the hull ruptures, crushing your body
                     into jam jelly."""% guess
            return 'death'
        else:
            print """
                     You jump into pod %s and hit the eject button.
                     The pod easily slides out into space heading to
                     the planet below.  As it flies to the planet, you look
                     back and see your ship implode then explode like a
                     bright star, taking out the Gothon ship at the same
                     time.  You won!"""% guess
            return 'finished'

class Finished(Scene):
    def enter (self):
        print "You won! Good job."
        return 'finished'

class Map(object): # Super Class

    scenes = {
        'central_corridor': Central_corridor(),
        'laser_weapon_armory': Laser_weapon_armory(),
        'the_bridge': The_bridge(),
        'escape_pod': Escape_pod(),
        'death': Death(),
        'finished': Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
