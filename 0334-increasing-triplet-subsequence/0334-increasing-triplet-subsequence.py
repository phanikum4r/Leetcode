class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        l, r = inf, inf
        for num in nums:
            if num <= l:
                l = num
            elif num <= r:
                r = num
            else:
                return True     
        return False