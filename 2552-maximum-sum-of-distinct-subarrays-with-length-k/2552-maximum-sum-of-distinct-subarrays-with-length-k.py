class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum, curSum = 0, 0
        start, end = 0, 0
        seen = {}
        while end < len(nums):
            cur = nums[end]
            idx = seen.get(cur, -1)
            while start <= idx or end - start >= k:
                curSum -= nums[start]
                del seen[nums[start]]
                start += 1
            seen[cur] = end
            curSum += cur
            if len(seen) == k:
                maxSum = max(maxSum, curSum)
            end += 1
        return maxSum