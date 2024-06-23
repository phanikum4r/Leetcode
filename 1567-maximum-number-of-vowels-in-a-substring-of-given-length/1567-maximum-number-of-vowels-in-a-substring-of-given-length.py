class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res=cur=len([i for i in s[:k] if i in "aeiou"])
        i,j=1,k
        while j<len(s):
            cur+=(s[j] in "aeiou")-(s[i-1] in "aeiou")
            if cur>res:
                res=cur
            j+=1
            i+=1
        return res