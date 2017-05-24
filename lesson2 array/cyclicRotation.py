 
a=[3, 8, 9, 7, 6] 
#a=[]
def solution(A, K):
    if len(A) == 0:
        return A

    array = A
    print(array)
    for i in range(K):
        buffer = array.pop()
        array.insert(0, buffer)
        print(array)
    return array

def solution2(A, K):
    # write your code in Python 2.7
    if len(A) == 0:
        return A
    
    K = K % len(A)
    print(A[-K:])
    print(A[:-K])
    return A[-K:] + A[:-K]    

print("array: {}".format(solution2(a, 1)))