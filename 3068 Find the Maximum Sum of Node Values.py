class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        numx = [x ^ k for x in nums]
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        dp = [[inf, inf] for _ in range(n)]

        def helper(node, parent):
            parity = 0
            score = 0
            smallestDiff = inf
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                helper(neigh, node)
                smallestDiff = min(smallestDiff, abs(dp[neigh][0] - dp[neigh][1]))
                if dp[neigh][0] < dp[neigh][1]:  # 
                    parity = 1 - parity
                    score += dp[neigh][1]
                else:
                    score += dp[neigh][0]
            dp[node][0] = max(score + (numx[node] if parity else nums[node]),
                              score - smallestDiff + (nums[node] if parity else numx[node]))
            dp[node][1] = max(score + (nums[node] if parity else numx[node]),
                              score - smallestDiff + (numx[node] if parity else nums[node]))
        helper(0, -1)
        return dp[0][0]
