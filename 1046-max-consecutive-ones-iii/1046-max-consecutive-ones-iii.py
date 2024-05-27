class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, zeros = 0,0,0
        n=len(nums)
        while right<n:
            if nums[right] == 0:
                zeros += 1
            right += 1
            if zeros>k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
        return right-left