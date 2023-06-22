class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        yes = -prices[0]
        no  = 0
        for p in prices[1:]:
            yes = max(yes, no-p)
            no  = max(no, yes+p-fee)
        return no        
