class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        sub, m = "", 0
        while end < len(s):
            start = sub.find(s[end])
            if start >= 0:
                sub = sub[start+1:] + s[end]
            else:
                sub += s[end]
            m = max(m, len(sub))
            end += 1
        return m