class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        result = 1
        for x1, y1 in points:
            d = defaultdict(int)
            for x2, y2 in points:
                if (x1, y1) != (x2, y2):
                    # try:
                    #     d[(y2 - y1) / (x2 - x1)] += 1
                    # except:
                    #     d[inf] += 1
                    d[atan2((y2 - y1) , (x2 - x1))] += 1
            result = max(result, max(d.values()) + 1)
        return result