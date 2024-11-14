class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, end = 0, 0
        result = []
        for i in range(1, len(nums)):
            if nums[i-1]!=nums[i]-1:
                if start == end:
                    result.append(f"{nums[start]}")
                else:
                    result.append(f"{nums[start]}->{nums[end]}")
                start, end = i, i
            else:
                end += 1
        if start == len(nums)-1:
            result.append(f"{nums[start]}")
        elif start<len(nums)-1:
            result.append(f"{nums[start]}->{nums[-1]}")
        return result
        
