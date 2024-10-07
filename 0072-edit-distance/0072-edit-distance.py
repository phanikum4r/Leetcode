class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        res=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        res[0]=[i for i in range(len(word2)+1)]
        for i in range(1,len(word1)+1):
            res[i][0]=i
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    res[i][j]=res[i-1][j-1]
                else:
                    res[i][j] = 1 + min(res[i][j-1], res[i-1][j], res[i-1][j-1])
        return res[len(word1)][len(word2)]