class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        c=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                diff=(nums[i-1]-nums[i]+1)
                c+=diff
                nums[i]+=diff
        return c