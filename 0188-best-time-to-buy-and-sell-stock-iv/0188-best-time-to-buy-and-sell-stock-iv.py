class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        # ~ performing unlimited transactions
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n - 1))

        dp_prev = [0] * n
        dp_curr = [0] * n
        for t in range(1, k + 1):
            # track the maximum of prices[j] - dp[t-1][j]
            max_diff = -prices[0]    
            for i in range(1, n):
                # Update dp_curr[i] considering either selling at day i or not
                dp_curr[i] = max(dp_curr[i-1], prices[i] + max_diff)
                max_diff = max(max_diff, dp_prev[i] - prices[i])
            dp_prev = dp_curr[:]
        return dp_curr[n-1]