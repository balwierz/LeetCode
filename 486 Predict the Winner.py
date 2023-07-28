class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def bestMove(arr):
            if not len(arr): return 0 
            return max(arr[0] - bestMove(arr[1:]), arr[-1] - bestMove(arr[:-1]))
        return bestMove(nums) >= 0
