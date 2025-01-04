class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        sub, m = "", 0
        while end < len(s):
            # check if the letter is seen, if not start =- 1
            start = sub.find(s[end])
            # if seen, new sub from right of seen index
            if start >= 0:
                sub = sub[start+1:] + s[end]
            else:
                sub += s[end]
            m = max(m, len(sub))
            end += 1
        return m