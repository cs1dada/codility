

def solution(A, B, K):
    count = 0
    for elem in range(A, B+1):
        if elem % K == 0:
            count += 1
    return count

"""
A % K = a
A = a + mK
A-A%K = a + mK - a = mK
[A,B] = [mK, B] = [0, B-mK] = [0, B-(A-A%K)]
"""
def solution2(A, B, K):
    if A % K == 0:  return (B - A) // K + 1
    else:           return (B - (A - A % K )) // K

print(solution(6,11,2))
