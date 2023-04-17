class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        scores = [-sum(num % d == 0 for num in nums) for d in divisors]
        return sorted(zip(scores, divisors))[0][1]
