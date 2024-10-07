class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # @lru_cache(maxsize=None)
        # def longest(index1,index2):
        #     if index1==len(text1) or index2==len(text2):
        #         return 0
        #     if text1[index1]==text2[index2]:
        #         return 1+longest(index1+1,index2+1)
        #     else:
        #         return max(longest(index1+1,index2),longest(index1,index2+1))
        # return longest(0,0)

        res=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    res[i][j]=1+res[i-1][j-1]
                else:
                    res[i][j]=max(res[i-1][j],res[i][j-1])
        return res[len(text1)][len(text2)]