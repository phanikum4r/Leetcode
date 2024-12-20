class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @cache
        # def dp(amount):
        #     if amount < 0:
        #         return -1
        #     if amount == 0:
        #         return 0
        #     res = inf
        #     for i in coins:
        #         val = dp(amount - i)
        #         if val != -1:
        #             res = min(res, 1 + val)
        #     return -1 if res==inf else res
        # return dp(amount)

        dp = [inf] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[-1] == inf else dp[-1]