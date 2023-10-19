class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def reduce(txt):
            ret = []
            for x in txt:
                if x == "#":
                    if len(ret) != 0:
                        ret.pop()
                else:
                    ret.append(x)
            return ret
        return reduce(s) == reduce(t)
