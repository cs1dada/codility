
'''
def solution(A):
    count_array = [0] * 100000
    miss_pivot = 0 # smallest int 1
    
    for elem in A:
        if elem > 0:
            # elem slot ++
            count_array[elem-1] += 1
            # elem == smallest int
            if miss_pivot == (elem-1):
                # go forward to find next smallest
                miss_pivot += 1
                while count_array[miss_pivot] > 0:
                    miss_pivot += 1
        else:
            continue

    return miss_pivot + 1
'''    
def solution(A):
    count_array = [0] * (len(A)+1)
    miss_pivot = 0 # smallest int 1
    
    for elem in A:
        if elem > 0 and elem < (len(A)+1):
            # elem slot ++
            count_array[elem-1] += 1
            # elem == smallest int
            if miss_pivot == (elem-1):
                # go forward to find next smallest
                miss_pivot += 1
                while count_array[miss_pivot] > 0:
                    miss_pivot += 1
        else:
            continue

    return miss_pivot + 1    

def solution2(A):
    ''' Solve it with Pigeonhole principle.
        There are N integers in the input. So for the
        first N+1 positive integers, at least one of
        them must be missing.
    '''
    # We only care about the first N+1 positive integers.
    # occurrence[i] is for the integer i+1.
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item-1] = True

    # Find out the missing minimal positive integer.
    for index in range(len(A) + 1):
        if occurrence[index] == False:
            return index + 1

    raise Exception("Should never be here.")
    return -1

array = [1,3,6,4,1,2]
#array = [-2147483648, 2147483647]
print(solution(array))