class Solution:
    def miceAndCheese2(self, reward1: List[int], reward2: List[int], k: int) -> int:
        gain = [(max(a,b) - min(a, b), int(b>a)) for a, b in zip(reward1, reward2)]
        gain.sort(reverse=True)
        left = [k, len(reward1)-k]
        ret = 0
        for g, mouse in gain:
            if left[mouse]:
                ret += g
                left[mouse] -= 1
        return ret + sum([min(a,b) for a, b in zip(reward1, reward2)])

    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        l = [i-j for i, j in zip(reward1, reward2)]
        l.sort(reverse=True)
        return sum(reward2) + sum(l[:k])
