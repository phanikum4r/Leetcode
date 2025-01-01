class Solution:
    def longestPalindrome(self, s: str) -> str:
        # using dp 2d array 
        # n = len(s)
        # start, end = 0, 0
        # dp = [[0] * n for _ in range(n)]
        # for i in range(n-1, -1, -1):
        #     for j in range(i + 1, n):
        #         dp[i][j] = (s[i] == s[j]) and (j-i <= 2  or dp[i+1][j-1])
        #         if dp[i][j] and (j - i > end - start):
        #             start, end = i, j
        # return s[start: end + 1]

        # expanding from centers O(n**2) O(1)
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            for j in (0, 1):
                left, right = i, i+j
                while left>=0 and right<n and s[left] == s[right]:
                    left -= 1
                    right += 1
                left += 1
                right -=1
                if right - left > end - start:
                    start, end = left, right
        return s[start: end + 1]