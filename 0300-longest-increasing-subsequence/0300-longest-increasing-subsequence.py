class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            x = bisect_left(res, num)
            if x == len(res):
                res.append(num)
            else:
                res[x] = num
        return len(res)