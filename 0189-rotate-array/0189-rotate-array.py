class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        def rev(nums,i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        rev(nums,0,n-k-1)
        rev(nums,n-k,n-1)
        rev(nums,0,n-1)
