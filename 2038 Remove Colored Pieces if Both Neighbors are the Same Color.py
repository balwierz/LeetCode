class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt = Counter()
        prev = ''
        i = 0
        for c in colors:
            if c == prev:
                i += 1
                if i >= 3:
                    cnt[c] += 1
            else:
                i = 1
                prev = c
        return cnt["A"] > cnt["B"]
