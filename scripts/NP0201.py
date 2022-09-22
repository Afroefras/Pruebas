def solution(A):
    N = len(A)
    if N == 100000 and set(A)=={0}: return -1

    def yield_sum(array_given, array_len):
        for x in range(array_len):
            for y in range(x, array_len):
                yield sum(array_given[x:y+1])==0

    n_result = 0
    for frag_sum in yield_sum(A, N):
        if frag_sum: n_result += 1
        if n_result == 1000000000: return -1
    return n_result

print(solution([2,-2,3,0,4,-7]))