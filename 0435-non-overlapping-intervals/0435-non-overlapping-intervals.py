class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        prev_end=-inf
        res=0
        for start, end in intervals:
            if start>=prev_end:
                prev_end=end
            else:
                res+=1
        return res