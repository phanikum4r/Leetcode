class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x, rev = abs(x), 0
        while x:
            x, rem = divmod(x, 10)
            rev = rev * 10 + rem
        return sign * rev if rev < 2**31 else 0
            