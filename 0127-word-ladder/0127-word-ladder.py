class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set(beginWord)
        q = deque([[beginWord, 1]])
        combinations = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                combinations[word[:i] + '*' + word[i+1:]].append(word)
        while q:
            cur, count = q.popleft()
            if cur == endWord:
                return count
            for i in range(len(cur)):
                for change in combinations[cur[:i] + '*' + cur[i+1:]]:
                    if change not in visited and change in wordList:
                        visited.add(change)
                        q.append([change, count + 1])
        return 0

        # time & space: O(len(word)**2 * len(wordList))