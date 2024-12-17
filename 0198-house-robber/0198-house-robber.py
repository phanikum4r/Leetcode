class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo={}
        # def dp(index):
        #     if index<0:
        #         return 0
        #     else:
        #         if index in memo:
        #             return memo[index]
        #         memo[index] = max(dp(index-2)+nums[index], dp(index-1))
        #         return memo[index]
        # return dp(len(nums)-1)


        if len(nums)==1:
            return nums[0]
        nums[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
                nums[i] = max(nums[i]+nums[i-2],nums[i-1])
        return nums[-1]


        # a, b = nums[0], nums[1]
        # for i in range(2, len(nums)):
        #     a, b = max(a, b), max(nums[i] + a, b)
        # return max(a, b)