class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin, curMax, minSum, maxSum, totalSum = 0, 0, nums[0], nums[0], 0
        for num in nums:
            curMin = min(curMin, 0) + num
            minSum = min(minSum, curMin)
            curMax = max(curMax, 0) + num
            maxSum = max(maxSum, curMax)
            totalSum += num
        if totalSum == minSum:
            return maxSum
        return max(maxSum, totalSum - minSum)