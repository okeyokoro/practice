name = "Zed A. Shaw"
age = 35 #So he says
height = 74 #inches
height_in_cm = height * 2.54

weight = 180 #Ib
weight_in_kg = weight * 0.453592

eyes = "Blue"
teeth = "White"
hair = "Brown"

print "Let's talk about %s."% name
print "He's %d centimeters tall."% height_in_cm
print "He's %d kg heavy."% weight_in_kg
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair."% (eyes,hair)
print "His teeth are usually %s depending on the cofee."% teeth
print "If I add %d,%d and %d I'll get %d"% (age,height_in_cm,weight_in_kg, age + height_in_cm + weight_in_kg)
