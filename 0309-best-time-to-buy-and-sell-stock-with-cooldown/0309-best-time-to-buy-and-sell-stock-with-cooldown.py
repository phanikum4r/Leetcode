class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash, hold, cooldown = 0, -prices[0], 0
        for i in range(1, len(prices)):
            cash, hold, cooldown = max(cash, hold + prices[i]), max(hold, cooldown - prices[i]), max(cooldown, cash)
        return max(cash, cooldown)

       