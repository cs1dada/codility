
array = [1,2,3,4,5,6,7,8,9]

def solution(A):
    length = len(A)
    
    summary = (1+(length+1))*(length+1)/2
    #print("{}, {}".format(length, summary))
    return summary - sum(A)

print(solution(array))