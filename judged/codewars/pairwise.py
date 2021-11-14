# pairwise([7, 9, 11, 13, 15], 20)
# this algorithm was written to pass the FreeCodeCamp Pairwise Challenge


def pairwise(origin, goal):
    result = []
    ans = []

    # destination = [], origin= [7, 9, 11, 13, 15]
    def pairperm(destination, origin):
        if len(destination) == 2:
            result.append(destination)
        else:
            for i in range(len(origin)):
                new_destination = destination + [origin[i]]
                new_origin = origin[i+1:]
                pairperm(new_destination, new_origin)

    pairperm([], origin)

    for arr in result:
        if sum(arr) == goal:
            ans.append(arr)

    print(ans or "Sorry No Results")

pairwise([7, 9, 11, 13, 15], 20)
