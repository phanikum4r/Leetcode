class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        if len(t) > len(s):
            return ""
        chars_in_t = defaultdict(int)
        remaining = len(t)
        start = 0
        left, right = 0, len(s)
        for ch in t:
            chars_in_t[ch] += 1
        
        for end in range(len(s)):
            if chars_in_t[s[end]] > 0:
                remaining -= 1
            chars_in_t[s[end]] -= 1
            if remaining == 0:
                while True:
                    if chars_in_t[s[start]] == 0:
                        break
                    chars_in_t[s[start]] += 1
                    start += 1
                
                if end - start < right - left:
                    left, right = start, end
                
                chars_in_t[s[start]] += 1
                remaining += 1
                start += 1
        
        return "" if right == len(s) else s[left: right + 1]