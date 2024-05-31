class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        k=prices[0]
        for i in prices:
            if i<k:
                k=i
            elif i-k>m:
                m=i-k
        return m