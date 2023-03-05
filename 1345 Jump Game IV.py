class Solution:
    def minJumps(self, arr: List[int]) -> int:
        val2ind = defaultdict(list)
        for i, v in enumerate(arr):
            val2ind[v].append(i)
        visited = [False for _ in range(len(arr))]
        visited[0] = True
        time = 0
        thisQ = [0]
        while(True):
            nextQ = []
            for ind in thisQ:
                if ind == len(arr) - 1:
                    return time
                if ind != 0 and not visited[ind-1]:
                    visited[ind-1] = True
                    nextQ.append(ind-1)
                if not visited[ind+1]:
                    visited[ind+1] = True
                    nextQ.append(ind+1)
                for w in val2ind[arr[ind]]:
                    if not visited[w]:
                        visited[w] = True
                        nextQ.append(w)
                val2ind[arr[ind]] = []
            thisQ = nextQ
            time += 1
