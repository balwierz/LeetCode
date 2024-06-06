class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        c = Counter(hand)
        for x in sorted(c.keys()):
            v = c[x]
            if v > 0:
                for y in range(x+1, x+groupSize):
                    c[y] -= v
                    if c[y] < 0:
                        return False
        return True
