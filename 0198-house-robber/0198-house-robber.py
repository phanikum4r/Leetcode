class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        x=0
        y=nums[0]
        for i in range(1,len(nums)):
            y,x=max(nums[i]+x, y),y
        return y