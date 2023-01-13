class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        # cut the tree into a forest
        numChildren = [0] * n
        for i, c in enumerate(s):
            if parent[i] != -1:
                if s[parent[i]] == c:
                    parent[i] = -1
                else:
                    numChildren[parent[i]] += 1

        longest = [0] * n
        secondLongest = [0] * n 
        ret = 1
        for i in range(n):
            if numChildren[i] == 0 and longest[i] == 0:  # true leaf
                invDepth = 0
                numChildren[i] = 1
                while i != -1:
                    if invDepth >= longest[i]:
                        secondLongest[i], longest[i] = longest[i], invDepth
                    elif invDepth > secondLongest[i]:
                        secondLongest[i] = invDepth
                    numChildren[i] -= 1
                    if numChildren[i] != 0:
                        break
                    ret = max(ret, longest[i] + secondLongest[i] + 1)
                    invDepth = longest[i] + 1
                    i = parent[i]
        return ret
