class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        @cache
        def dfs(i : int, balance: Tuple[int]) -> int:
            if i == len(requests):
                return 0 if all(b == 0 for b in balance) else float('-inf') 
            bal = list(balance)
            bal[requests[i][0]] -= 1
            bal[requests[i][1]] += 1
            return max(1 + dfs(i + 1, tuple(bal)), dfs(i + 1, balance))
        return dfs(0, tuple([0] * n))


    def maximumRequests2(self, n: int, requests: List[List[int]]) -> int:
        ret = 0
        r = len(requests)
        def check(state):
            buildings = [0] * n
            for i in range(r):
                if state & (1 << i):
                    buildings[requests[i][0]] -= 1
                    buildings[requests[i][1]] += 1
            for b in buildings:
                if b:
                    return False
            return True
        
        for state in range(2**r):
            if check(state):
                ret = max(ret, state.bit_count())
        return ret
