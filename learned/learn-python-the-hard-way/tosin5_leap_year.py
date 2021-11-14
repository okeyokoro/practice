# This is aprogram to determine whether a year is leap year or nah
def leap_or_nah (year):
    if year%4 == 0:
        print "\nYup, that's a leap year. Trust me, I know one when I see one. =)\n"
    elif type(year) != int:
        print "\n That's not a year dummy\n"    
    else:
        print "\nNope. Not a leap year\n"


year = input("\nInput Year>>>")

leap_or_nah(year)
