class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node['#'] = True

    def search(self, word: str) -> bool:
        def find(word, node):
            for i in range(len(word)):
                if word[i] == '.':
                    for j in node:
                        if j!="#" and find(word[i+1:], node[j]):
                            return True
                    return False
                if word[i] not in node:
                    return False
                node = node[word[i]]
            return ('#' in node)
        return find(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)