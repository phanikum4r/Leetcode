class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memo={}
        # def dp(index):
        #     if index in memo:
        #         return memo[index]
        #     if index>len(cost)-3:
        #         memo[index]=cost[index]
        #     else:
        #         memo[index] = min(dp(index+1),dp(index+2))+cost[index]
        #     return memo[index]
        # return min(dp(0),dp(1))
        
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])