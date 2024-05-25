class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def findsubset(nums,i,subset):
            if i==n:
                subsets.append(subset[:])
            else:
                subset.append(nums[i])
                findsubset(nums,i+1,subset)
                subset.pop()
                findsubset(nums,i+1,subset)
        n=len(nums)
        subsets=[]
        findsubset(nums,0,[])
        return subsets