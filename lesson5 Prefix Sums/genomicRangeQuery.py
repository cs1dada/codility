
def solution(S, P, Q):
    M = len(P)
    dna = list(S) # N
    impact = list()
    minfactor = list()
    count = 4
    print(dna)

    for elem in range(M):
        impact.append(dna[P[elem]:Q[elem]+1])
    print(impact)

    for elem in impact:
        for factor in elem:
            if factor == "A" and count > 1:
                count = 1
            elif factor == "C" and count > 2:
                count = 2
            elif factor == "G" and count > 3:
                count = 3
            elif factor == "T" and count > 4:
                count = 4
        minfactor.append(count)
        count = 4
    return minfactor

def solution2(S, P, Q):
    n = len(S)
    sumA = [0]*(n+1)
    sumC = [0]*(n+1)
    sumG = [0]*(n+1)
    sumT = [0]*(n+1)

    for  index, nuleotide in enumerate(S): #O(N) SUM
        sumA[index+1] = sumA[index]
        sumC[index+1] = sumC[index]
        sumG[index+1] = sumG[index]
        sumT[index+1] = sumT[index]
        if nuleotide == 'A':
            sumA[index+1] += 1
        elif nuleotide == 'C':
            sumC[index+1] += 1
        elif nuleotide == 'G':
            sumG[index+1] += 1
        elif nuleotide == 'T':
            sumT[index+1] += 1
    print(sumA)
    print(sumC)
    print(sumG)
    print(sumT)

    reult = [0]*len(P)
    for elem in range(len(P)): #O(M)
        Afactor = sumA[Q[elem]+1] - sumA[P[elem]] #1
        Cfactor = sumC[Q[elem]+1] - sumC[P[elem]] #2
        Gfactor = sumG[Q[elem]+1] - sumG[P[elem]] #3
        Tfactor = sumT[Q[elem]+1] - sumT[P[elem]] #4

        if Afactor > 0:
            reult[elem] = 1
        elif Cfactor > 0:
            reult[elem] = 2
        elif Gfactor > 0:
            reult[elem] = 3
        else:
            reult[elem] = 4

    return reult


string = "CAGCCTA"    
p = [2,5,0]
q = [4,5,6]
#string = "A"
#p = [0]
#q = [0]

print(solution2(string,p,q))