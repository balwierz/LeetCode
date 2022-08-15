class Solution:
    def smallestNumber(self, pattern: str) -> str:
        lowestNum = 1
        dLen = 0
        iLen = 1
        last = "I"
        pattern += "ID"
        ret = ""
        for s in pattern:
            if(s == "D"):
                dLen+=1
                if last == "I":
                    for i in range(lowestNum, lowestNum + iLen - 1):
                        ret += str(i)
                    lowestNum += iLen - 1
                last = "D"
                iLen = 0
            else:
                iLen+=1
                if last == "D":
                    for i in range(lowestNum+dLen, lowestNum-1, -1):
                        ret += str(i)
                    lowestNum += dLen + 1
                last = "I"
                dLen = 0
        return ret
        
