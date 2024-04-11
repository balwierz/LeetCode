class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): return "0"
        data = [0]*128
        for h in num[:k+1]:
            data[ord(h)] += 1
        i = 0
        ret = []
        while k:
            # choose the lowest digit from c to keep:
            keep = ord('0')
            while data[keep] == 0:
                keep += 1
            ret.append(chr(keep))
            while k and ord(num[i]) != keep:
                k -= 1
                data[ord(num[i])] -= 1
                i += 1
            i += 1
            data[keep] -= 1
            if i+k == len(num):
                break
            data[ord(num[i+k])] += 1
        ret = ''.join(ret)
        if k == 0:
            ret += num[i:]            
        # remove leading zeros
        ret = ret.lstrip("0")
        return ret if ret else "0" 
