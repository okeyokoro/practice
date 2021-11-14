from math import sqrt

def calculate_distance(p1, p2):
    return sqrt(
        (p2[0] - p1[0])**2
        + (p2[1] - p1[1])**2
    )

def find_max_element(arr):
    """ arr = [ (d, point), (d, point) ]"""
    ans = [-1, None]
    for i in range(len(arr)):
        if arr[i][0] > ans[0]:
            ans[0] = arr[i][0]
            ans[1] = i
    return ans # (distance, index)


class Solution:
    def kClosest(self, points, k_closest, vertex=[0,0]):
        if not k_closest:
            return []

        arr = []

        for point in points:
            reached_capacity = len(arr) >= k_closest
            d = calculate_distance(point, vertex)

            if not reached_capacity:
                arr.append( (d, point) )
                continue

            mx = find_max_element(arr) # instead of iterating to find the maximum element, everytime, just use a max-heap
            if d < mx[0]:
                arr[mx[1]] = (d, point)

        return [ i[1] for i in arr ]
        # time complexity: O(n*k),  best-case: O(n), worst-case: O(n*n)
        # space complexity: O(k)
