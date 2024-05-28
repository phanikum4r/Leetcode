class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n):
            if (nums[i]>=n-i):
                if i==0:
                    return n-i
                elif ((n-i) > nums[i-1]):
                    return n-i  
        return -1