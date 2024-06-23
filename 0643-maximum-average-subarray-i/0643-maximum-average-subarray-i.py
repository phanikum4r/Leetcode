class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=s=sum(nums[0:k])
        i,j=1,k
        while j<len(nums):
            s+=(nums[j]-nums[i-1])
            if s>res:
                res=s
            j+=1
            i+=1
        return res/k