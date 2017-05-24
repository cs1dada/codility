import sys
#O(n)
def solution(N):
	binary = list()
	binary = bin(int(N))

	start = False
	count = 0
	maximun = 0

	for value in binary:

		if value == "1" and start == False:
			start = True
		elif value == "0" and start == True: 
			count += 1
		elif value == "1" and start == True:
			if count > maximun:
				maximun = count
			count = 0
		print("{} {}".format(value, count))

	print("gap: {}".format(maximun))
	return maximun

#O(logn)
def solution2(N):
    N = int(N)
    max_gap = 0
    current_gap = 0
 
    # Skip the tailing zero(s)
    while N > 0 and N%2 == 0:
        N //= 2
 
    while N > 0:
        remainder = N%2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2
 
    return max_gap

def solution3(N):
    N = int(N)
    #gaps = "{0:b}".format(N).split('1')[1:-1]
    gaps = "{0:b}".format(N)[1:-1]
    print(gaps)
    return len(max(gaps)) if gaps else 0

arg = sys.argv
if len(arg) != 2:
	print("input error: ")
	for element in arg:
		print(element)
else:
	number = arg[1]
	print(solution3(number))

