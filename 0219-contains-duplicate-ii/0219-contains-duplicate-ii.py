class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Time Efficient
        d = {}
        for i, n in enumerate(nums):
          if n in d and abs(i - d[n]) <= k:
            return True
          else:
            d[n] = i
        return False

        # Space Efficient
        # s = []
        # last = 0
        # if k==0:
        #     return False
        # for i in nums:
        #     if i in s:
        #         return True
        #     if len(s)<k:
        #         s.append(i)  
        #     else:
        #         last %= k
        #         s[last] = i
        #     last += 1
        # return False