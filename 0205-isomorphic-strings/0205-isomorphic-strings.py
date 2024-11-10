class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if t[i] != d[s[i]]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
        return True