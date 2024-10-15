class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dcount=senate.count('D')
        rcount=len(senate)-dcount
        rban=0
        dban=0
        q=deque(senate)
        while q:
            if dcount==0:
                return 'Radiant'
            if rcount==0:
                return 'Dire'
            if q.popleft()=='R':
                if rban:
                    rban-=1
                    rcount-=1
                else:
                    dban+=1
                    q.append('R')
            else:
                if dban:
                    dban-=1
                    dcount-=1
                else:
                    rban+=1
                    q.append('D')