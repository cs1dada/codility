

def solution(X, A):
    count = 0
    index = 0
    count_array = [False] * (X+1)

    for elem in A:
        if elem < (X+1):
            if count_array[elem] == False:
                count_array[elem] = True
                count += 1
                if count == X:
                    return index
        index += 1
    return -1

#array = [1,3,1,4,2,3,5,4]
array = [1]
length = 6
print(solution(length, array))









