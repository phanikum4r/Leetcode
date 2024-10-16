class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count('1') + bin(((a & b) | c) ^ c).count('1')

        # if position has 1 in both a and b, and 0 in c, 
        # we need to count one more time as we are replacing twice. 
        # second count checks this scenario