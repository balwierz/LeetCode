class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ret = 1000000
        state = [0] * k
        if k == len(cookies):
            return max(cookies)
        def helper(j):
            nonlocal cookies
            nonlocal ret
            nonlocal state
            if j == len(cookies):
                ret = min(ret, max(state))
            else:
                for i in range(k):
                    state[i] += cookies[j]
                    helper(j+1)
                    state[i] -= cookies[j]
        helper(0)
        return ret
