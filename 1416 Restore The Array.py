class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def helper(pos: int):
            if pos == n: 
                return 1
            if s[pos] == '0':
                return 0        
            leftInt = 0
            ret = 0
            for i in range(pos, n):
                leftInt = 10 * leftInt + (ord(s[i]) - ord('0'))
                if leftInt > k:
                    break
                ret += helper(i+1)
                ret %= 1_000_000_007
            return ret

        return helper(0)
