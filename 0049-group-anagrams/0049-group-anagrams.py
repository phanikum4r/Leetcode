class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(NKlogK)
        d=defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return list(d.values())

        # O(NK)
        # d = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c)-ord('a')] += 1
        #     d[tuple(count)].append(s)
        # return list(d.values())