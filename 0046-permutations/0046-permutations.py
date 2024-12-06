class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(arr):
            for i in range(len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    if len(arr) == len(nums):
                        result.append(arr[:])
                    else:
                        backtrack(arr)
                    arr.pop()
        backtrack([])
        return result