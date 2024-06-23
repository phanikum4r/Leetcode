class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        res=0
        for x in count.keys():
            if k-x in count:
                res+=(min(count[x],count[k-x]))
        return res//2