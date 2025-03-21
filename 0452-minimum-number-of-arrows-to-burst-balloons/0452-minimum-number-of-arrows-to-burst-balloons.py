class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        prev_end = -inf
        ans=0
        for start, end in points:
            if start>prev_end:
                ans+=1
                prev_end = end
        return ans