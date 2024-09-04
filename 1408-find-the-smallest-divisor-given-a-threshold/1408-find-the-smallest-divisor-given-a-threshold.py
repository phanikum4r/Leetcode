class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        high=max(nums)
        low=1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            res=0
            for dividend in nums:
                res+=math.ceil(dividend/mid)
                if res>threshold:
                    break
            if res>threshold:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans