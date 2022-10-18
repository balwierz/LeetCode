class Solution:
    def countAndSay(self, n: int) -> str:
        txt = "1"
        for i in range(2, n+1):
            last = txt[0]
            cnt = 0
            newTxt = ''
            for d in txt:
                if d == last:
                    cnt += 1
                else:
                    newTxt += str(cnt) + last
                    cnt = 1
                    last = d
            newTxt += str(cnt) + last
            txt = newTxt
        return txt
