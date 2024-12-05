class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for i in word:
                if i not in node:
                    node[i] = {}
                node = node[i]
            node['*'] = word
        result = []
        def backtrack(r, c, parent):
            letter = board[r][c]
            cur = parent[letter]
            if '*' in cur:
                result.append(cur.pop('*'))
            board[r][c] = '#'
            for x, y in [(-1,0), (0, -1), (1, 0), (0, 1)]:
                if r+x < 0 or r+x >= len(board) or c+y < 0 or c+y >= len(board[0]):
                    continue
                if board[r+x][c+y] in cur:
                    backtrack(r+x, c+y, cur)
            board[r][c] = letter
            if not cur:
                parent.pop(letter)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        return result