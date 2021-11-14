def square_or_nah(num):
    root = num**0.5
    if num == int(root)**2 :
        result = "\n%d is a perfect square\n"% num
    else:
        result = "\n%d is not a perfect square\n"% num
    print result


def to_improper_fraction(d):
    dec = str(d)
##########################################################
    length=len(dec.split('.')[1])
    top = int(dec.split('.')[1])
#########################################################
    bottom = 10**length

    root_top = top**0.5
    root_bottom = bottom**0.5

    if top == int(root_top)**2 and bottom == int(root_bottom)**2 :
        result = "\n%f is a perfect square\n"% d
    else:
        result = "\n%f is not a perfect square\n"% d
    print result


number = input("\nInput number >>>")

if type(number) == int :
    square_or_nah(number)
else:
    to_improper_fraction(number)
