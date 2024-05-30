class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twosum(nums,target,left):
            i,j = left, len(nums)-1
            res=[]
            while i<j:
                if i>left and nums[i-1]==nums[i]:
                    i+=1
                elif nums[i]+nums[j]>target:
                    j-=1
                elif nums[i]+nums[j]<target:
                    i+=1
                else:
                    res.append([nums[i],nums[j]])
                    i+=1
                    j-=1
            return res
        nums.sort()
        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j,k in twosum(nums,-nums[i],i+1):
                result.append([nums[i],j,k])
        return result