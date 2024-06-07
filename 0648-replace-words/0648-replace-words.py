class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sen=sentence.split(" ")
        for i in range(len(sen)):
            word=sen[i]
            j=0
            while j<len(word):
                if word[0:j+1] in dictionary:
                    sen[i]=word[0:j+1]
                    break
                j+=1
        return " ".join(sen)