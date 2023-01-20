class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        cand = set()   #candidates. must be at least 1 char in len
        ret = []
        n = len(nums)
        for num in nums:
            # try extending existing candidates:
            newCand = set()
            for c in cand:
                print(c)
                if num >= c[-1]:
                    newSeq = tuple(c + tuple([num]))
                    if newSeq not in cand:
                        newCand.add(newSeq)
                        ret.append(newSeq)
            # start a new candidate:
            cand |= newCand
            cand.add(tuple([num]))
        return ret
