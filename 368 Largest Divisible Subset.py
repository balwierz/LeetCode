import sortedcontainers

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        len2data = sortedcontainers.SortedDict(lambda x: -x)
        len2data[1] = []
        for x in nums:
            isFound = False
            for l in iter(len2data):
                for i, seq in enumerate(len2data[l]):
                    if x % seq[-1] == 0:
                        if l+1 not in len2data:
                            len2data[l+1] = []
                        len2data[l+1].append(seq.copy())
                        len2data[l+1][-1].append(x)
                        isFound = True
                        break
                if isFound:
                    break
            if isFound:
                continue
            len2data[1].append([x])
        return len2data.popitem(0)[1][0]
