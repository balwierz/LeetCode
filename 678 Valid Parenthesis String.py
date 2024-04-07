class Solution:
    def checkValidString(self, s: str) -> bool:
        s = list(s)
        stack = []
        nStar = 0
        for i, x in enumerate(s):
            if x == "(":
                stack.append(i)
            elif x == ")":
                if stack:
                    j = stack.pop()
                    s[j] = s[i] = "_"
                else:
                    if nStar:
                        nStar -= 1
                    else:
                        return False
            else: # *
                nStar += 1
        #print("".join(s))
        # right to left
        nStar = 0
        for x in reversed(s):
            if x == "(":
                if nStar:
                    nStar -= 1
                else:
                    return False
            elif x == "*":
                nStar += 1
        return True


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0,0

        for c in s:
            if c == "(":
                lo, hi = lo + 1, hi + 1
            elif c == ")":
                lo, hi = lo - 1, hi -1
            else:
                lo = lo - 1
                hi = hi + 1
            if hi < 0:
                return False
            if lo < 0:
                lo = 0
        return lo==0
