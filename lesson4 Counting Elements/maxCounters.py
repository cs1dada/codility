
# O(n^2), len(A) = M
def solution(N, A):
    max_value = 0
    count_array = [0] * N
    for elem in A:
        if elem <= N:
            count_array[elem-1] += 1
            if count_array[elem-1] > max_value:
                max_value = count_array[elem-1]
        elif elem == N+1:
            for index in range(N):
                count_array[index] = max_value

    return count_array

def solution2(N, A):
    max_value = 0 # immediate max
    tmp_max_value = 0 # for late max

    #maxop = [False] * N # record max operation
    count_array = [0] * N

    for elem in A:
        if elem <= N:# inc_op
            # late maxify
            if count_array[elem-1] < tmp_max_value:
                count_array[elem-1] = tmp_max_value
            #inc
            count_array[elem-1] += 1
            # update max_value
            if count_array[elem-1] > max_value:
                max_value = count_array[elem-1]
            #print("inc_op")
            #print(count_array)
        elif elem == N+1: # max_op
            # cache max_value for late use
            tmp_max_value = max_value
            #print("max_op")
            #print(count_array)

    for index in range(0, N):
        if count_array[index] < tmp_max_value:
            count_array[index] = tmp_max_value

    return count_array

n = 5
array = [3,4,4,6,1,4,4]
print(solution2(n,array))

