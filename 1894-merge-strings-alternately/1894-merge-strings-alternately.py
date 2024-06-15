class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        n1=len(word1)
        n2=len(word2)
        result=[]
        while i<n1 or j<n2:
            if i<n1:
                result.append(word1[i])
                i+=1
            if j<n2:
                result.append(word2[j])
                j+=1
        return "".join(result)