class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret2 = [0] * (len(nums))  # bit array (bits can be larger than 1) represending binary representation of the answer 
        # at first it will hold compressed intervals!
        i = 0
        singletons = 0
        for j in range(len(nums)-1, -1, -1):
            if i <= j:
                while i<=j and nums[i] + nums[j] <= target:
                    i += 1
                # i is now at the first wrong index
                # either larger than j or for which the condition is not met
                if i == 0: # the condition is not met at all
                    continue
                longestArr  = j  # actually one larger than longest Arr
                shortestArr = j - i
                if shortestArr < 0: # special case when max == min
                    shortestArr = 0
                    singletons += 1  # we observe an additional array [j,j]
            else: # we know that 2*nums[j] <= target
                longestArr = j # again, longest array + 1
                shortestArr = 0
                singletons += 1
            ret2[shortestArr] += 1
            ret2[longestArr]  -= 1

        # now we have ret2 ready and singletons to add in the end
        pow2 = 1
        height = ret2[0]
        ret = singletons + height
        for i in range(1, len(nums)-1):
            height += ret2[i]
            pow2 += pow2
            pow2 %= 1_000_000_007
            ret = (ret + height * pow2) % 1_000_000_007
        return ret
