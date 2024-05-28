class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        m=logs[0][0:2]
        for i in range(len(logs)):
            diff=logs[i][1]-logs[i-1][1]
            if diff>m[1]:
                m[0],m[1]=logs[i][0],diff
            if diff == m[1]:
                m[0]=min(m[0],logs[i][0])
        return m[0]