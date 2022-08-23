class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        bh = (intLength+1) // 2   #bigger half
        start = 10**(bh-1)
        ret = [0] * len(queries)
        for (i, q) in enumerate(queries):
            q = q - 1 # start counting from 0th index
            end = start + q
            if(len(str(end)) > bh ):
                ret[i] = -1
            else:
                endstr = str(end) + str(end)[::-1][int(bh + bh != intLength):]
                ret[i] = int(endstr)
        return ret
