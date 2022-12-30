class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        out = [set() for _ in range(n+1)]
        for a, b in edges:
            out[a].add(b)
            out[b].add(a)
        isOdd = [len(s) % 2 for s in out]
        odd = [i for i, v in enumerate(isOdd) if v]
        def joinTwo(a, b):
            for v in range(1, n+1):
                if v not in out[a] and v not in out[b]:
                    return True
            return False
        
        numOdd = len(odd)
        if numOdd == 0:
            return True
        if numOdd > 4 or numOdd % 2 == 1:
            return False
        if numOdd == 2:
            if odd[0] not in out[odd[1]]:    # it means vice versa too
                return True
            return joinTwo(odd[0], odd[1])
        if numOdd == 4: # last possibility
            if odd[1] not in out[odd[0]] and odd[3] not in out[odd[2]]:
                return True
            if odd[2] not in out[odd[0]] and odd[1] not in out[odd[3]]:
                return True
            if odd[3] not in out[odd[0]] and odd[1] not in out[odd[2]]:
                return True
        return(False)
