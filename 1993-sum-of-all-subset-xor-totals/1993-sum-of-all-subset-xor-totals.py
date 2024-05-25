class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def findxor(nums,i,cxor):
            if i==n:
                return cxor
            withindex=findxor(nums,i+1,cxor^nums[i])
            without=findxor(nums,i+1,cxor)
            return withindex+without
        n=len(nums)
        return findxor(nums,0,0)
