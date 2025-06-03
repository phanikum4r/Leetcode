class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = max_avg = sum(nums[:k])
        i = 0
        for j in range(k, len(nums)):
            avg += nums[j] - nums[i]
            max_avg = max(avg, max_avg)
            i += 1
        return max_avg/k