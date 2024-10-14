class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                if j-i>1:
                    nums[i+1], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
        return i+1