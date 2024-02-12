class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = [Counter([x%d for x in nums]).most_common(1)[0][0] for d in (7,11,13,17,19)]
        for x in nums:
            if [x%7, x%11, x%13, x%17, x%19] == data:
                return x
        
    def majorityElement(self, nums: List[int]) -> int:
        count = 0    
        for num in nums:
            if count == 0:
                candidate = num
            count += [-1,1][num == candidate]
        return candidate
