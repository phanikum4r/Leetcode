class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix)!=0:
                if prefix=="":
                    return ""
                else:
                    prefix = prefix[:-1]
        return prefix