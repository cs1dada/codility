
def solution(A):
    count_array = [0] * len(A)
    
    for elem in A:
        if elem - 1 >= len(A):
            return 0

        count_array[elem -1] += 1

    for index in range(len(A)):
        if count_array[index] > 1 or count_array[index] == 0:
            return 0

    return 1

#array = [4,1,3,2]
#array = [4,1,3]
#array = [1]
array = [1,2,4,5,5]
print(solution(array))    