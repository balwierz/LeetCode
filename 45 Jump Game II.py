class Solution:
    def jump(self, nums: List[int]) -> int:
        s = [0, 0]  # keeps positions to check in the next step
        time = 0
        while True:
            if s[1] >= len(nums)-1:
                return time
            time += 1
            furthestStep = max([pos+nums[pos] for pos in range(s[0], s[1]+1)])
            s = [s[1]+1, furthestStep]
