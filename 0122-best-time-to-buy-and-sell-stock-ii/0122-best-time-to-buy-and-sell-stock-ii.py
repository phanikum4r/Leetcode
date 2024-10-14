class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for price in prices:
            if price - buy > 0:
                profit += price - buy
            buy = price
        return profit