class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        result = []
        for i in range(1, len(nums)):
            if nums[i-1]!=nums[i]-1:
                if start == i-1:
                    result.append(f"{nums[start]}")
                else:
                    result.append(f"{nums[start]}->{nums[i-1]}")
                start = i
        if start == len(nums)-1:
            result.append(f"{nums[start]}")
        elif start<len(nums)-1:
            result.append(f"{nums[start]}->{nums[-1]}")
        return result
        
