# def hats():
#     cats = [0]*100
#     for num in range(100):
#         cats = round(num, cats)
#     print [ i for i,k in enumerate(cats) if cats[i]==1 ]
#     print [ i for i,k in enumerate(cats) ]


# def round(num, cats):
#     for i in range(0,100,num+1):
#         if cats[i]:
#             cats[i] = 0
#         else:
#             cats[i] = 1
#     return cats

# hats()

# theCats = {}

# for i in range(1, 101):
#     theCats[i] = False

# print theCats

# for i in range(1, 101):
#     for cats, hats in theCats.items():
#         if cats % i == 0:
#             if theCats[cats]:
#                 theCats[cats] = False
#             else:
#                 theCats[cats] = True

# for cats, hats in theCats.items():
#     if theCats[cats]:
#         print("Cat {} has a hat.".format(cats))
#     else:
#         print("Cat {} is hatless!".format(cats))