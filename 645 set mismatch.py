class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ret = [0, 0]
        for i in range(1, len(nums)+1):
            if cnt[i] == 2:
                ret[0] = i
            if cnt[i] == 0:
                ret[1] = i
        return ret
