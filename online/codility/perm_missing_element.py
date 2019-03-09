def solution(A):
    diffs = [ abs(sum(A[1:])-A[0]) ]
    right = sum(A[1:])
    left = A[0]
    for i in range(1,len(A)-1):
        right -= A[i]
        left += A[i]
        diffs.append(abs(right-left))
    return sorted(diffs)[0]
