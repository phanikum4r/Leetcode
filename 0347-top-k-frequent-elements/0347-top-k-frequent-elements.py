class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i, j in sorted(Counter(nums).items(), key = lambda x: x[1], reverse = True)[: k]]