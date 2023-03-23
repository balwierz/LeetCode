class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [1]
        for i in range(1, n):
            nums.append(i*nums[i-1])
        digits = list(range(1,n+1))
        k -= 1
        ret = ""
        for num in reversed(nums):
            a, b = divmod(k, num)
            ret += str(digits[a])
            digits.remove(digits[a])
            k = b

        return ret
