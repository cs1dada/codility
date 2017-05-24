import functools

test = [9,3,9,3,9,7,9]
print("test: {}".format(test))

def solution(A):
    return functools.reduce(lambda x,y: x^y, A, 0)

# a xor a = 0, a xor 0 = a, a xor a xor c xor b xor c = b
def solution2(A):
    initval=0
    for elem in A:
        initval = elem ^ initval
    return initval

print(solution2(test))

