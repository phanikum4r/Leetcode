class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            # cash can be from previous cash or sell now and get cash
            cash = max(cash, hold + prices[i] - fee)
            # hold from previous hold or buy with existing cash
            hold = max(hold, cash - prices[i])
        return cash