class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        i,j,k=0,n-1,n-1
        while i<=j:
            a,b=nums[i]**2, nums[j]**2
            if a>=b:
                res[k]=a
                i+=1
            else:
                res[k]=b
                j-=1
            k-=1
        return res