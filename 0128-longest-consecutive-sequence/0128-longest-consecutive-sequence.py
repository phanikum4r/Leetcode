class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                current_len = 1
                current_num = num
                while current_num + 1 in nums:
                    current_len += 1
                    current_num += 1
                longest = max(longest, current_len)
        return longest