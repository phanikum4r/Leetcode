class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            else:
                profit += price - buy
                buy = price
        return profit

        # profit = 0
        # for i in range(1, len(prices)):
        #     profit += max(prices[i] - prices[i - 1], 0)
        # return profit