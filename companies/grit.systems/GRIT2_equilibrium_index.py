def solution(A):
    right = sum(A[2:])
    left = A[0]
    diffs = []
    if right == left:
        diffs.append(1)
    for i in range(2, len(A)):
        right -= A[i]
        left += A[i-1]
        if right == left:
            diffs.append(i)
    # print diffs
    print diffs[0] if len(diffs) > 0 else -1

solution([-1, 3, -4, 5, 1, -6, 2, 1])
