class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        col = [0] * (n+1)  # to make sure ends are accounted for
        cur = 0
        for i, c in queries:
            if c != col[i]:
                # removal:
                if col[i] != 0:
                    if col[i-1] == col[i]:
                        cur -= 1
                    if col[i+1] == col[i]:
                        cur -= 1
                # add
                if col[i-1] == c:
                    cur += 1
                if col[i+1] == c:
                    cur += 1
            yield cur
            col[i] = c
