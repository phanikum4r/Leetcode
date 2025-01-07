class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        p, q = location
        extra = 0 
        angles = []
        for x, y in points:
            if p == x and q == y:
                extra += 1
            else:
                # convert each point to angle from location
                angles.append(atan2((y - q), (x - p)) * 180 / pi)

        angles.sort()
        # adding angles from 2nd half in circle
        angles = angles + [x + 360 for x in angles]
        start, end = 0, 0
        maxPoints = 0
        while end < len(angles):
            while angles[end] - angles[start] > angle:
                start += 1
            maxPoints = max(end - start + 1, maxPoints)
            end += 1
        return maxPoints + extra