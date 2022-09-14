class Solution:
    def partitionString(self, s: str) -> int:
        run = set()
        ret = 1;
        for c in s:
            if c in run:
                ret += 1
                run.clear()
            run.add(c)
        return ret
