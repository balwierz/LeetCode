class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        ret = 0  #defaultdict(int)
        cnt = 0
        child = [[] for _ in range(n)]
        for i in range(1, n):
            child[parents[i]].append(i)
        def dfs(v):
            nonlocal ret, cnt
            #print(str(v))
            subtreeLen = []
            for c in child[v]:
                subtreeLen.append(dfs(c))
            
            thisScore = 1
            if len(subtreeLen) >= 1:
                thisScore *= subtreeLen[0]
            if len(subtreeLen) == 2:
                thisScore *= subtreeLen[1]
            if v != 0:
                thisScore *= n - sum(subtreeLen) - 1
            if thisScore > ret:
                ret, cnt = thisScore, 1
            elif thisScore == ret:
                cnt += 1
            #ret[thisScore] += 1
            return sum(subtreeLen) + 1       
        
        dfs(0)
        return cnt
        #return(ret[max(ret.keys())])
