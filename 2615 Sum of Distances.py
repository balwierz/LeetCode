class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        data = defaultdict(int)   # value to return
        count = defaultdict(int)  # number of elems to the right - num elem to the left
        for i, num in enumerate(nums):
            data[num] += i
            count[num] += 1
        
        lastPos = {num:0 for num in data}
        # we will return nums
        for i, num in enumerate(nums):
            data[num] -= (i - lastPos[num]) * count[num]
            lastPos[num] = i
            count[num] -= 2
            nums[i] = data[num]

        return nums
