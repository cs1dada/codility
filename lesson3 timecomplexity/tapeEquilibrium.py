
def solution(A):
    buffer = list()
    sum = 0
    index = 0
    pivot = 0
    absolute = 0
    result = 0
    rightsum = 0

    for elem in A:
        result += elem
        buffer.append(result)
        #print(buffer)
    
    sum = buffer.pop()
    #absolute = abs(sum)

    for elem in buffer:
        rightsum = sum - elem
        temp = abs(elem - rightsum)
        #print("rightsum:{}, temp:{}".format(rightsum, temp))
        #temp = abs(sum - 2*elem)
        if index == 0:
            absolute = temp
        elif temp < absolute:
            #print("{},{},{}".format(elem,temp, absolute))
            absolute = temp
            pivot = index+1
        index += 1

    return absolute


def solution2(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)

    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)

    return min_dif

a = [1,-2,3,4,5,6]
print(solution(a))