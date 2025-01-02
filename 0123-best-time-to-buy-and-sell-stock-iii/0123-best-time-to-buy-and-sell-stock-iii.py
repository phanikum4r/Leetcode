class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  with left and right prefix arrays dp
        # n = len(prices)
        # left, right = [0] * n, [0] * n
        # buy = prices[0]  
        # for i in range(1, n):
        #     left[i] = max(left[i-1], prices[i] - buy)
        #     if prices[i] < buy:
        #         buy = prices[i]
        # sell = prices[-1]
        # for i in range(n - 2, -1, -1): 
        #     right[i] = max(right[i+1], sell - prices[i])
        #     if prices[i] > sell:
        #         sell = prices[i]
        #     left[i] += right[i + 1]
        # return max(left)

        # buy 1 buy 2 sell 1 sell 2 one pass O(n) & O(1)
        buy1, buy2 = inf, inf
        profit1, profit2 = 0, 0
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
               
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
        return profit2