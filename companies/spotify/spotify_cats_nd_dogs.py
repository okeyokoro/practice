# spotify cats vs dogs problem

# cats and dogs on tv show
# one animal is evicted every week

# voters cast two votes about 
# 1. which animal should stay 
# 2. which animal should leave 
# the two votes must contain one cat and one dog

# programmust ensure that maximum number of viewers continue to watch the show
# this may mean ensuring that the most liked cat and most liked dog stay on
# the show as long as possible
# following the assumption that most viewers are either cat or dog people

# the program should return the maximum number of viewers

no_of_testcases = raw_input("number_of_testcases >> ")

# for loop here for each test case, and input for each

no_of_cats, no_of_dogs, no_of_voters = raw_input("no_of_cats no_of_dogs no_of_voters >> ").split(" ")

no_of_testcases, no_of_cats, no_of_dogs, no_of_voters = int(no_of_testcases),\
                               int(no_of_cats), int(no_of_dogs), int(no_of_voters)

print no_of_cats


# def maximum_views(no_of_testcases,
#                   no_of_cats, no_of_dogs, no_of_voters,
#                   ):
#     # big sean reference
#     if no_of_testcases > 100:
#         return "no_of_testcases must be <= 100"
#     elif no_of_cats < 1:
#         return "no_of_cats must be >= 1"
#     elif no_of_dogs > 100:
#         return "no of dogs <= 100"
#     elif 0 > no_of_voters > 500:
#         return "no_of_voters must be 0 <= and <= 500"

#     for testcase in range(no_of_testcases):
#         ##
#         for voter in range(no_of_voters):
#             ##
#             vote(stay_pet, leave_pet)
