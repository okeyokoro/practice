# python 3

# I wrote this while trying to solve the No Repeats Please Challenge
# on FCC. I really learnt about recursion by watching some youtube videos
# just search 'Recursion Stanford' - the course is Programming
# Abstractions

def permute(so_far, remaining):
    if not remaining:
        print(so_far)
    else:
        for i in range(len(remaining)):
            new_so_far = so_far + remaining[i]
            new_remaining = remaining[0:i] + remaining[i+1:]
            permute(new_so_far, new_remaining)

def wrapper(string_to_perm):
    permute("", string_to_perm)

while True:
    string_to_perm = input("Enter String to be permutated >>")

    if type(string_to_perm) is str:
        wrapper(string_to_perm)
    else:
        print("Input a string please")
