

def solution(A):
    pair = 0
    count = 0
    for elem in A:
        if elem == 0:
            pair += 1
        elif elem == 1:
            count += pair
    if count > 1000000000:
        count = -1
    return count

array = [0,1,0,1,1]
print(solution(array))
