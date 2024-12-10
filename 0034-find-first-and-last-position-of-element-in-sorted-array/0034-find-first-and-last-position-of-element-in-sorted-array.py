class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target and (mid == left or nums[mid - 1] < target):
                start = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target and (mid == right or nums[mid + 1] > target):
                end = mid
                break
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return [start, end]