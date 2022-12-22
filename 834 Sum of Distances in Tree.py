class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Part 0: build the unrooted tree as a bidir, symmetrical graph:
        neigh = [[] for _ in range(n)]
        for a, b in edges:
            neigh[a].append(b)
            neigh[b].append(a)
        # Part 1: Root the tree at zero node and calcule num nodes in subtree, and frontSum of distances coming from the parts of tree down below a given node
        nNodes =   [0 for _ in range(n)]
        frontSum = [0 for _ in range(n)]

        def dfs0(node, parent):
            # sets the number of nodes including itself when coming from parent
            # returns sum of distances and the number of children
            sumDist = 0
            nChild = 0
            for v in neigh[node]:
                if v == parent: 
                    continue
                s, c = dfs0(v, node)
                sumDist += s + c
                nChild += c
            nChild += 1 # count itself
            nNodes[node] = nChild
            frontSum[node] = sumDist
            return ((sumDist, nChild))
        dfs0(0, -1)
    
        # part 2: another dfs which fills the values in the return array, by recalculating the number of backNodes and backSum
        ret = [0 for _ in range(n)]
        def dfs1(node, parent, backNodes, backSum):
            ret[node] = backSum + frontSum[node]
            for v in neigh[node]:
                if v == parent:
                    continue
                dfs1(v, node, 
                    backNodes + nNodes[node] - nNodes[v], 
                    backSum + backNodes + nNodes[node] - nNodes[v]*2 + frontSum[node] - frontSum[v] )
        dfs1(0, -1, 0, 0)
        return ret
