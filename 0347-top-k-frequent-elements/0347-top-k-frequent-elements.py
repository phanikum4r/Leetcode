class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [i for i, j in sorted(Counter(nums).items(), key = lambda x: x[1], reverse = True)[: k]]
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res