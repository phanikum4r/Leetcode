class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # memo={}
        # def dp(idx):
        #     if idx == len(nums)-1:
        #         return True
        #     if idx >= len(nums):
        #         return False
        #     if idx in memo:
        #         return memo[idx]
        #     count=nums[idx]
        #     while count>0:
        #         if dp(idx+count):
        #             memo[idx] = True
        #             return True
        #         count-=1
        #     memo[idx] = False
        #     return False
        # return dp(0)

        last_pos=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i>=last_pos:
                last_pos=i
        return not last_pos    