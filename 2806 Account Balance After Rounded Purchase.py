class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return (100-purchaseAmount+4) // 10 * 10
