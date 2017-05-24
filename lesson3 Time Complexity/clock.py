
class Solution(object):
    def clock(self, S, T):
        count = 0
        startSec = self.tranToSec(S)
        endSec = self.tranToSec(T)

        
        print("startSec:{}, endSec:{}".format(startSec, endSec))
        
        for sec in range(startSec, endSec+1):            
            hour   = self.secToTime(sec)[0]
            minute = self.secToTime(sec)[1]
            second = self.secToTime(sec)[2]
            #[hour,minute,second]
            interest = list(str(hour)) + list(str(minute)) + list(str(second))
            print(interest)
            print(set(interest))
            print(len(set(interest)))

            if len(set(interest)) <= 2:
                count += 1
        return count
        

    def tranToSec(self, string):
        strBuf = list(string)
        print(strBuf)
        return (int(strBuf[0])*10 + int(strBuf[1]))*60*60 + \
               (int(strBuf[3])*10 + int(strBuf[4]))*60 + \
               (int(strBuf[6])*10 + int(strBuf[7]))

    def secToTime(self, sec):
        time = []

        hour   = int(sec) // (60 * 60)
        if hour < 10:
            hour = str("0") + str(hour)         
        time.append(hour)

        minute = (int(sec) % (60 * 60)) // 60
        if minute < 10:
            minute = str("0") + str(minute)         
        time.append(minute)

        second = (int(sec) % (60 * 60)) % 60
        if second < 10:
            second = str("0") + str(second) 
        time.append(second)

        #print(time)
        return time #[hour,minute,second]



if __name__ == "__main__":
    #print(Solution().bracket("()()()()()"))
    #print(Solution().bracket("(())))("))   
    #print(Solution().clock("00:00:00","00:00:10"))
    print(Solution().clock("15:15:00","15:15:12"))