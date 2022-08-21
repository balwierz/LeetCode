class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ret = []
        nReplBig = -1
        while(nReplBig):
            nReplBig = 0
            for sz in range(len(stamp), 0, -1):  # loop over stamp size
                #print("sz=" + str(sz))
                for i in range(0, len(stamp)-sz+1):
                    nReplaced = -1
                    while(nReplaced):
                        nReplaced = 0
                        #print("i=" + str(i))
                        patt = "0" * i + stamp[i:i+sz] + "0" * (len(stamp)-sz-i)
                        #print(patt)
                        it = re.finditer(patt, target)
                        foo = [int(it.start()) for it in it]
                        nReplaced += len(foo)
                        ret.extend(foo)
                        target = re.sub(patt, "0"*len(stamp), target)
                        #print(target)
                        nReplBig += nReplaced
            if target == "0" * len(target):
                ret.reverse()
                return ret
        #return [6,3,2,0]
        return []
