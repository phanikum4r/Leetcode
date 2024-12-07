class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], 0
        for num in nums:
            curSum += num
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        return maxSum