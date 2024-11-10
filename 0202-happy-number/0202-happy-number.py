class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            s = 0
            while n:
                digit = n % 10
                n //= 10
                s += digit*digit
            return s

        # slow = n
        # fast = get_next(get_next(n))
        # while slow != 1 and slow != fast:
        #     slow = get_next(slow)
        #     fast = get_next(get_next(fast))
        # return slow == 1

        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1