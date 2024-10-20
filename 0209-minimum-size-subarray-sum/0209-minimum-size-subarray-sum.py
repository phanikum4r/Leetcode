class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        s, m = 0, inf
        while end < len(nums):
            s += nums[end]
            while s >= target:
                m = min(end-start+1, m)
                s -= nums[start]
                start += 1
            end += 1
        return 0 if m==inf else m