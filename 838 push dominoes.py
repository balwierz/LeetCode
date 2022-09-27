class Solution:
    def pushDominoes(self, dom: str) -> str:
        ret = ['.'] * len(dom)
        lastPos = -1
        lastDir = -1  # left
        for i in range(len(dom)):
            if dom[i] == '.':
                if lastDir == -1:
                    ret[i] = "."
                else:
                    ret[i] = 'R'
            if dom[i] == "R":
                lastDir = 1
                lastPos = i
                ret[i] = "R"
            if dom[i] == "L":
                if lastDir == -1:
                    for j in range(lastPos+1, i+1):
                        ret[j] = "L"
                else:  # lstDir==R
                    for j in range((lastPos + i) // 2 + 1 , i+1):
                        ret[j] = "L"
                    if (i - lastPos) % 2 == 0:  # uneven num of dominos in between, there is a central one
                        ret[(lastPos + i) // 2] = "."
                    lastPos = i
                    lastDir = -1
        return ''.join(ret)
            
