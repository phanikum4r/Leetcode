class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        res=[]
        for spell in spells:
            res.append(n-bisect.bisect_left(potions, ceil(success/spell)))
        return res