class Solution:
    def strangePrinter(self, s: str) -> int:
        s = re.sub(r'(.)\1*', r'\1', s)
        @cache
        def solve(l, r):
            if len(s) <= 2:
                return len(s)
            if s[0] == s[-1]:
                return solve(s[:-1])
            cost = solve(s[:-1]) + 1
            char = s[-1]
            for i, letter in enumerate(s[:-1]):
                if char == letter:
                    cost = min(cost, solve(s[:i]) + solve(s[i:-1]))
            return cost
        
        return solve(s)  
