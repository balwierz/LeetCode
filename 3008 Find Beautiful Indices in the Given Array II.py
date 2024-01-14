class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        kmp = KMP()
        allA = kmp.search(s, a) + [999999999]
        allB = kmp.search(s, b)
        ia = 0
        ret = []
        coverage = [0] * (len(s) + 1)
        for m in allB:
            coverage[max(0, m-k)] += 1
            coverage[min(len(s), m+k+1)] -= 1
        lvl = 0
        for i, x in enumerate(coverage):
            lvl += x
            if allA[ia] == i:
                if lvl > 0:
                    ret.append(i)
                ia += 1
        return ret

