class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heappop(heap)
        return [[x, y] for _, x, y in heap]