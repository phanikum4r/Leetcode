class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sen=sentence.split(" ")
        dict_set=set(dictionary)
        for i in range(len(sen)):
            word=sen[i]
            for j in range(len(word)):
                if word[0:j+1] in dict_set:
                    sen[i]=word[0:j+1]
                    break
        return " ".join(sen)