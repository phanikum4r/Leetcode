class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start,end,zeros=0,0,0
        while end<len(nums):
            if nums[end]==0:
                zeros+=1
            if zeros>k:
                if nums[start]==0:
                    zeros-=1
                start+=1
            end+=1
        return end-start