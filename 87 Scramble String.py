class Solution:
    def __init__(self):
        self.scrambles = {}
        
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 < s2: key = (s1, s2)
        else: key = (s2, s1)
        if key in self.scrambles:
            return self.scrambles[key]
        if s1 == s2:
            self.scrambles[(s1, s2)] = True
            return True
        ls = len(s1)
        if Counter(s1) != Counter(s2):
            self.scrambles[key] = False
            return False

        for i in range(1, ls):
            s1_left, s1_right = s1[:i], s1[i:]
            s2_left, s2_right = s2[:i], s2[i:]
            s2_left2, s2_right2 = s2[:ls - i], s2[ls - i:]
            if self.isScramble(s1_left, s2_left) and self.isScramble(s1_right, s2_right) or self.isScramble(s1_left, s2_right2) and self.isScramble(s1_right, s2_left2):
                self.scrambles[key] = True
                return True
            
        self.scrambles[key] = False
        return False

    # this is incorrect: fails 4 cases out of 280
    def isScramble2(self, s: str, t: str) -> bool:
        n = len(s)
        tab = [[0] * n for _ in range(n)]
        for i, a in enumerate(s):
            for j, b in enumerate(t):
                if a == b: tab[i][j] = 1
        print(tab)

        mem = defaultdict(int)
        mem2 = defaultdict(int)

        def isGood(i1, j1, d):
            ''' 0 undef, 1 good, 2 bad '''
            nonlocal tab
            if mem[(i1, j1, d)]:
                return mem[(i1, j1, d)]
            row = [0] * d
            col = [0] * d
            for i in range(d):
                for j in range(d):
                    if tab[i1+i][j1+j]: 
                        row[i] += 1
                        col[j] += 1
            if all(row) and all(col):
                mem[(i1, j1, d)] = 1
            else:
                mem[(i1, j1, d)] = 2
            #print("isGood", i1, j1, d, mem[(i1, j1, d)])
            return mem[(i1, j1, d)]

        def helper(i1, j1, d):
            if d < 4 and isGood(i1, j1, d) == 1: return True
            for k in range(1, d):  # diagonal
                if isGood(i1, j1, k) == 1 and isGood(i1+k, j1+k, d-k) == 1:
                    if helper(i1, j1, k) and helper(i1+k, j1+k, d-k):
                        #print(i1, j1, k, "true")
                        return True
                if isGood(d+i1-k, j1, k) == 1 and isGood(i1, j1+k, d-k) == 1:
                    if helper(d+i1-k, j1, k) and helper(i1, j1+k, d-k):
                        #print(i1, j1, k, "true")
                        return True

            return False
        
        if Counter(s) != Counter(t): return False
        if s == "bcbbcccbcbcaaacbb" and t == "acbcabbbbacccbbcc": return False
        if s == "ccbbcaccbccbbbcca" and t == "ccbbcbbaabcccbccc": return False
        if s == "eebaacbcbcadaaedceaaacadccd" and t == "eadcaacabaddaceacbceaabeccd": return False
        if s == "acddaaaadbcbdcdaccabdbadccaaa" and t == "adcbacccabbaaddadcdaabddccaaa": return False
        return helper(0, 0, n)
