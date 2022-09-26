from numpy import *
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # separate equalities (and build a reachability graph from it via Floyd-Warshall)
        # from inequalities. Then go over all the inequalities and if arguments are reachable
        # form each other. If there exist a reachable pair return False. Otherwise True.
        # we will have at most 26 variables and at most 500 equations. Having a matrix equality
        # representation is fine.
        
        isEqual = eye(26, dtype="bool")
            
        for eq in equations:
            if eq[1] == "=":
                i = ord(eq[0]) - ord('a')
                j = ord(eq[3]) - ord('a')
                isEqual[i, j] = True
                isEqual[j, i] = True
        
        for k, i, j in permutations(range(26), 3):
            isEqual[i, j] |= isEqual[i, k] and isEqual[k, j]
                
        #for k in range(26):
        #    for i in range(26):
        #        for j in range(26):
        #            if isEqual[i, k] and isEqual[k, j]:
        #                isEqual[i, j] = True
                        
        for eq in equations:
            if eq[1] == "!":
                i = ord(eq[0]) - ord('a')
                j = ord(eq[3]) - ord('a')
                if isEqual[i, j]:
                    return False
                
        return True

## the fastest solution is via union-find:

class UF:
    def __init__(self, n):
        self.parent = []

        for i in range(n):
            self.parent.append(i)

    def find(self, x):
        # find the root of x

        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, p, q):
        # connect p and q
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        self.parent[rootQ] = rootP

    def connected(self, p, q):
        # check if p and q connected
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
    
class Solution2:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UF(26)
        
        eq_set = []
        neq_set = []
        
        for eq in equations:
            
            a, b = ord(eq[0])-ord('a'), ord(eq[-1])-ord('a')
            
            if eq[1] == '=':
                eq_set.append([a, b])
                
            else:
                neq_set.append([a, b])
                
        for [a,b] in eq_set:
            uf.union(a, b)
            
        for [a,b] in neq_set:
            
            a = uf.find(a)
            b = uf.find(b)
            if a==b:
                return False
            
        return True
