class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([[startGene, 0]])
        visited = set(startGene)
        while q:
            cur, mutations = q.popleft()
            if cur == endGene:
                return mutations
            for i in range(len(cur)):
                for ch in 'ACGT':
                    change = cur[:i] + ch + cur[i+1:]
                    if change not in visited and change in bank:
                        visited.add(change)
                        q.append([change, mutations + 1])
        return -1