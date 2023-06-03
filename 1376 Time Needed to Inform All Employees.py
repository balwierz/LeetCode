class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                children[m].append(i)
        def inform(x):
            # returns max time to inform subtree
            ret = 0
            for child in children[x]:
                ret = max(ret, inform(child))
            return ret + informTime[x]
        return inform(headID)
