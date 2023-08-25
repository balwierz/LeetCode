class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        data = [len(nums)] * 4
        for num in nums:
            data[num] -= 1
            for i in range(num, 3):
                if data[i+1] > data[i]:
                    data[i+1] = data[i]
        return data[3]        

class Solution2:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        left =  list(accumulate(nums, lambda x, y: x + int(y != 1), initial=0))
        right = list(accumulate(reversed(nums), lambda x, y: x + int(y != 3), initial = 0))[::-1]
        mid = list(accumulate(nums, lambda x, y: x + int(y != 2), initial = 0))
        ret = 100
        for i in range(0, n+1):
            for j in range(i, n+1):
                ret = min(ret, left[i] + right[j] + mid[j] - mid[i])
        return ret
