from math import sqrt

def calculate_distance(p1, p2):
    return sqrt(
        (p2[0] - p1[0])**2
        + (p2[1] - p1[1])**2
    )

class Solution:
    def kClosest(self, points, k_closest, vertex=[0,0]):
        q = []
        for point in points:
            q.append((calculate_distance(point, vertex),
                      point,))

        q = sorted(q, key=lambda x: x[0]) # sort by smallest distance
        q = [ i[1] for i in q ]
        return q[0:k_closest]

        # time-complexity: O(nlogn)
        # space complexity: O(n)

# ------------------------
# Two-liner from leetcode:
# ------------------------

class Solution(object):
    def kClosest(self, points, K, vertex=[0,0]):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]

# OR
