from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        res={0:1}
        for i in range(1,len(rooms)):
            res[i]=0
        q=deque()
        for j in rooms[0]:
            res[j]+=1
            q.append(j)
        while q:
            l=rooms[q.popleft()]
            for j in l:
                if res[j]==0:
                    res[j]=1
                    q.append(j)
        for k in res.values():
            if k==0:
                return False
        return True