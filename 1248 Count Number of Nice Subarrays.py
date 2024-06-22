class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        data, numEven = [], 0
        for x in chain([0], nums, [1]):
            if x&1:
                data.append(1+numEven)
                numEven = 0
            else:
                numEven += 1
        data[0] -= 1
        return sum(data[i] * data[i-k] for i in range(k, len(data)))
