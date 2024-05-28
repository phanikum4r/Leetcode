class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c=0
        d=Counter(nums)
        for num in nums:
            if (num+k) in d:
                c+=d[num+k]
            if (num-k) in d:
                c+=d[num-k]
        return c//2    