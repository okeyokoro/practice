#define the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "\nYou have %d cheeses!"% cheese_count
    print "You have %d boxes of crackers!"% boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

#passing arguments through the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# we can pass variables through the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#doing math as arguments
print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

#study drill
def beer_and_girls(sixpack, peng):
    print "You've got %d sixpacks of beer!"% sixpack
    print "%d babes are coming thru!!"% peng
    print "Issa party!!! \n"

print "Study Drill Challenge: Come up with af function and run it 10 different ways\n"
#1
beer_and_girls(7,80)
#2
beer_and_girls(5+90,560/10)

beer = 41
girls = 900
#3
beer_and_girls(beer, girls)
#4
beer_and_girls(beer+12,girls+67)

beer_input = input("How much beer you got? :")
girls_input = input("How many peng things are coming thru? :")
#5
beer_and_girls(beer_input, girls_input)
#6
beer_and_girls(beer_input+10, girls_input+34)
#7
beer_and_girls(beer_input+beer, girls_input+girls)
#Functional Programming
#8
def get_beer():
     return 45

def get_girls():
     return 23

put_beer = get_beer()
put_girls = get_girls()

beer_and_girls(put_beer, put_girls)
#9
beer_and_girls(get_beer(), get_girls())
#10
def get_more_beer():
    beer = input("Me drink beer. How much beer you got? : ")
    return beer
def get_more_girls():
    girls = input("I dont do sausage parties. How much peng can I be expecting? :")
    return girls

beer_and_girls(get_more_beer(), get_more_girls())
