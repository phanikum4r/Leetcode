class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                low = mid+1
            elif mid > 0 and nums[mid] < nums[mid-1]:
                high = mid-1
            else:
                return mid