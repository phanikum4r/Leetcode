class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for price in prices:
            profit += max(0, price-buy)
            buy = price
        return profit