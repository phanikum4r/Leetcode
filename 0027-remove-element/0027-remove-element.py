class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j,count = 0, len(nums)-1, 0
        while i<=j:
            if nums[i]==val:
                count+=1
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
            else:
                i+=1
        return len(nums)-count