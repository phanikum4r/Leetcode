class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = []
        last = 0
        if k==0:
            return False
        for i in nums:
            if i in s:
                return True
            if len(s)<k:
                s.append(i)  
            else:
                last %= k
                s[last] = i
            last += 1
        return False