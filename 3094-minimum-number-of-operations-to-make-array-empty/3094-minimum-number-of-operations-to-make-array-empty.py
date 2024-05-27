from collections import Counter
from math import ceil
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0
        for val in count.values():
            if val==1:
                return -1
            res+= ceil(val/3) 
        return res