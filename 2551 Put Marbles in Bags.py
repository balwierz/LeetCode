class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        data  = [weights[i]+weights[i+1] for i in range(n-1)]
        data2 = data.copy()
        heapify(data)
        a = [heappop(data) for _ in range(k-1)]
        data2 = [-d for d in data2]
        heapify(data2)
        b = [-heappop(data2) for _ in range(k-1)]
        return sum(b) - sum(a)
        print(data2)
        return 0
        #return sum(data[n-k:n-1]) - sum(data[0:k-1])
