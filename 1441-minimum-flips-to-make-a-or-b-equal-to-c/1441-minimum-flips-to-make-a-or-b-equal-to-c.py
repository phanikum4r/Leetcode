class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count('1') + bin(((a & b) | c) ^ c).count('1')