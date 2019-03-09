# This exercise is about dictionaries <---- They don't have order

states = {
    'Oregon':'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities =  {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-'*10
print 'NY State has: ',cities['NY']
print 'OR State has: ',cities['OR']

print '-'*10
print "Michigan's abbreviation is: ",states['Michigan']
print "Florida's abbreviation is: ",states['Florida']

print '-'*10
print 'Michigan has: ',cities[states['Michigan']]
print 'Florida has: ',cities[states['Florida']]

# Print every states abbreviation
print '-'*10
for state, abbrev in states.items():
    print "%s is abbreviated %s"% (state, abbrev)

print '-'*10
for abbrev, city in cities.items():
    print "%s has the city %s"% (abbrev, city)
print '-'*10

for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s"% (state, abbrev, cities[abbrev])

print '-'*10

# safely get abbreviation for non existent state
state = states.get('Texas')

if not state:
    print 'Sorry, no Texas.'

# get a city with default value

city = cities.get('TX','Does not exist')
print "the city for the state 'TX' is: %s"% city

print states.items() # This returns a list of tuples eg. [(k1,v1),(k2,v2),....(kn,vn)] <---- key-value pairs

# This is a cool program to count the number of times a character occurs in a sentence
sentence = "The quick brown fox jumped over the lazy dog."
characters = {}

for character in sentence:
    characters[character] = characters.get(character, 0) + 1

print characters
