class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if intervals[i][1]<newInterval[0]:
                result.append(intervals[i])
            elif newInterval[1]<intervals[i][0]:
                result.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval[0] = min(intervals[i][0],newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        result.append(newInterval)
        return result