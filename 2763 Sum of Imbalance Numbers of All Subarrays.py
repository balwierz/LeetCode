class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ret = 0
        for start in range(len(nums)):
            seen = set([nums[start]])
            imbalance = 0
            for end in range(start+1, len(nums)):
                val = nums[end]
                if val in seen:
                    ret += imbalance
                    continue
                if val-1 not in seen and val+1 not in seen:
                    imbalance += 1
                if val-1 in seen and val+1 in seen:
                    imbalance -= 1
                ret += imbalance
                seen.add(val)
        return ret
