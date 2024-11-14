class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        flag = 0
        for i in range(len(intervals)):
            if flag:
                if intervals[i][0]<=result[-1][1]:
                    result[-1][1] = max(result[-1][1], intervals[i][1])
                else:
                    result.append(intervals[i])
            elif intervals[i][1]<newInterval[0]:
                result.append(intervals[i])
            elif newInterval[1]<intervals[i][0]:
                result.append(newInterval)
                result.append(intervals[i])
                flag = 1
            elif newInterval[0]<=intervals[i][1]:
                intervals[i][0] = min(intervals[i][0],newInterval[0])
                intervals[i][1] = max(intervals[i][1], newInterval[1])
                result.append(intervals[i])
                flag = 1
        return result if flag else result+[newInterval]