class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = [i for i in range(len(word2)+1)]
        for i in range(1,len(word1)+1):
            cur = [i]*(len(word2)+1)
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    cur[j]=prev[j-1]
                else:
                    cur[j] = 1 + min(cur[j-1], prev[j], prev[j-1])
            prev = cur
        return prev[-1]