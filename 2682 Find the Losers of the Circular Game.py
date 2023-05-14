class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = {0}
        x = 0
        step = k
        while True:
            x += step
            x %= n
            if x in seen:    # end of the game
                return [f+1 for f in range(n) if f not in seen]
            seen.add(x)
            step += k
