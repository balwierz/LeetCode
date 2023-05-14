class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)//2
        ret = 0
        pairsLeft = n
        pairs = []
        used = [False] * (2*n)
        def helper():
            nonlocal pairsLeft, ret
            if pairsLeft == 0:
                sortedPairs = sorted(pairs)
                ret = max(ret, sum(sortedPairs[i] * (i+1) for i in range(n)))
            else:
                # find first not used pair
                i = 0
                while used[i]: i += 1
                used[i] = True
                pairsLeft -= 1
                # for each unused j later make a pair:
                for j in range(i+1, 2*n):
                    if not used[j]:
                        used[j] = True
                        pairs.append(gcd(nums[i], nums[j]))
                        helper()
                        used[j] = False
                        pairs.pop()        
                used[i] = False
                pairsLeft += 1
        helper()
        return ret


