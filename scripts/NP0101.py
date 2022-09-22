def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        else:
            l = m
    if A[l] == X:
        return l
    return -1


print('[1,2,5,9,9], 5: ', solution([1,2,5,9,9], 5))
print('[], 5: ', solution([], 5))
print('[], 5: ', solution([], 5))
print('[1], 5: ', solution([1], 5))
print('[1], 1: ', solution([1], 1))
print('[0], 0: ', solution([0], 0))
print('[-1], 0: ', solution([-1], 0))
print('[1,2], 1: ', solution([1,2], 1))
print('[1,2], 3: ', solution([1,2], 3))
print('[-1], -1: ', solution([-1], -1))
print('[-2,-1], -1: ', solution([-2,-1], -1))
print('[-2,-1], -3: ', solution([-2,-1], -3))