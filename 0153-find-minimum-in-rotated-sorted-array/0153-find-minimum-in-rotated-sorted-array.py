class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if (mid == left or nums[mid - 1] > nums[mid]) and (mid == right or nums[mid] < nums[mid + 1]):
                return min(nums[0], nums[mid])
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[0]