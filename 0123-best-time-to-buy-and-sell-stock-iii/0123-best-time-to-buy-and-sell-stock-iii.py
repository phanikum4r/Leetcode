class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  with left and right prefix arrays dp
        n = len(prices)
        left, right = [0] * n, [0] * n
        buy = prices[0]
        for i in range(1, n):
            left[i] = max(left[i-1], prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]

        sell = prices[-1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i+1], sell - prices[i])
            if prices[i] > sell:
                sell = prices[i]
            left[i] += right[i + 1]
        return max(left)