class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        if len(word1)!=len(word2):
            return False
        if set(c1.keys())!=set(c2.keys()):
            return False
        if sorted(c1.values())!=sorted(c2.values()):
            return False
        return True