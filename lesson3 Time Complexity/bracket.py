
class Solution(object):
    def bracket(self, s):
        bracketBuf = list(s)

        head = 0
        tail = len(bracketBuf) - 1
        print(tail)
        openBracket = 0
        closeBracket = 0

        stopHead = False
        stopTail = False

        while head < tail:
            if bracketBuf[head] == '(' and not stopHead:
                openBracket += 1

            if bracketBuf[tail] == ')' and not stopTail:
                closeBracket += 1

            print("openBracket {}, closeBracket {}".format(openBracket,closeBracket))

            if openBracket <= closeBracket:
                head += 1
                stopHead = False
            else:
                stopHead = True

            if closeBracket <= openBracket:
                tail -= 1
                stopTail = False
            else:
                stopTail = True

            print("head {}, tail {}".format(head,tail))
            

        return head

    def bracket2(self, s):
        bracketBuf = list(s)

        head = 0
        tail = len(bracketBuf) - 1
        #print(tail)
        openBracket = 0
        closeBracket = 0

        while head < tail:
            if bracketBuf[head] != '(':
                head += 1
            elif bracketBuf[tail] != ')':
                tail -=1
            else:
                openBracket += 1
                closeBracket += 1
                head += 1
                tail -=1

        if head == tail:
            return head+1
        else:
            return head



if __name__ == "__main__":
    print(Solution().bracket2("()()()()()"))
    print(Solution().bracket2("(())))("))   
    print(Solution().bracket2("((())))("))     