from collections import Counter
from math import ceil
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for val in Counter(nums).values():
            if val==1:
                return -1
            c+= ceil(val/3) 
        return c