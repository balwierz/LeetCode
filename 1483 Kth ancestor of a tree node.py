class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.anc = []
        parent.append(-1)
        self.anc.append(parent)
        i = 0
        #while not all([self.anc[i][j] == -1 for j in range(n+1)]):
        while i<=15:
            self.anc.append([self.anc[i][self.anc[i][j]] for j in range(n+1)])
            i += 1
        
        

    def getKthAncestor(self, node: int, k: int) -> int:
        i = 0
        while k:
            if k & 1:
                node = self.anc[i][node]
                if node == -1: return -1
            i += 1
            k >>= 1
            
            #u = k & -k
            #s = int(log2(u))
            #print(str(s) + " " + str(node))
            #node = self.anc[s][node]
            #k = k-u
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k
