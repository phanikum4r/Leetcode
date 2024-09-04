class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros, m = 0,0
        for i in s:
            if i=='0':
                zeros+=1
            else:
                m=max(m+(zeros!=0),zeros)
        return m