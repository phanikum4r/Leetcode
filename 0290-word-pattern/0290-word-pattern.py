class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split(" ")
        pattern=list(pattern)

        if len(s)!=len(pattern):
            return False
        
        for i in range(len(s)):
            if s[i] in d:
                if pattern[i] != d[s[i]]:
                    return False
            else:
                if pattern[i] in d.values():
                    return False
                d[s[i]] = pattern[i]
                
        return True