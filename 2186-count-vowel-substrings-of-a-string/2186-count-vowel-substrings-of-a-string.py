class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res=0
        for i in range(len(word)):
            l=['a','e','i','o','u']
            for j in range(i,len(word)):
                if word[j] in 'aeiou':
                    if word[j] in l:
                       l.remove(word[j]) 
                    res+=(not l)
                else:
                    break
        return res