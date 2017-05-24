
def solution(X, Y, D):
    '''
    X+D*n >= Y
    D*n >= Y-X
    n >= (Y-X)/D
    '''
    if (Y-X)%D == 0:
        return int((Y-X)/D)
    else:
        return int((Y-X)/D+1)


print(solution(1,1,3))