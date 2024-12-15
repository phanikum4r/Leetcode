class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
        # count = 0
        # while n:
        #     count += n % 2
        #     n >>= 1
        # return count