from copy import copy
from bisect import bisect
from collections import defaultdict
from pprint import pprint as print

def apartmentHunting(blocks, reqs):
    """
        question
            find any apartment with the smallest distance to all my requirements
        pre-conditions
        topic
        twist
        test
        brute-force
        complexity-ladder
        code
        execute
    """
    
    init = { req: float("inf") for req in reqs }
    block_i_distance_from_req =  [ copy(init) for b in blocks ]
    
    blocks_with = defaultdict(list) # "gym" : [ 1, 3]
    
    for req in reqs:
        for i, b in enumerate(blocks):
            if b[req] == True:
                block_i_distance_from_req[i][req] = 0
                blocks_with[req].append(i)
    
    # O( n x m x m )
    for i, b in enumerate(block_i_distance_from_req):
        for req in reqs:
            if b[req] == float("inf"):
                b[req] = min([ abs(j - i) for j in blocks_with[req] ])
    
    total_distances = [ max(b.values()) for b in block_i_distance_from_req ]
    # changed from 'sum' to 'max'
    
    result = None
    min_result = float("inf")
    
    for i,d in enumerate(total_distances):
        if d < min_result:
            min_result = d
            result = i
    
    print(block_i_distance_from_req)
    print(total_distances)
    
    return result
