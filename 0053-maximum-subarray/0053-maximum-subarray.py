class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=nums[0]
        cur_sum=0
        for num in nums:
            cur_sum+=num
            if cur_sum>maximum:
                maximum=cur_sum
            if cur_sum<0:
                cur_sum=0
        return maximum