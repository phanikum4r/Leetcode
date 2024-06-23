class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start=end=flip=0
        while end<len(nums):
            if nums[end]==0:
                flip+=1
            if flip>1:
                if nums[start]==0:
                    flip-=1
                start+=1
            end+=1
        return end-start-1