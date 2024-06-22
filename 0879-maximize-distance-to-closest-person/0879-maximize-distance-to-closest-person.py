class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start,end=0,0
        m,c=0,0
        for i in range(len(seats)):
            if seats[i]==1:
                start=i
                break
        for i in range(len(seats)-1,-1,-1):
            if seats[i]==1:
                end=i
                break
        m=max(len(seats[:start]),len(seats[end:])-1)
        for i in seats:
            if i==0:
                c+=1
                m=max(m,(c+1)//2)
            else:
                c=0
        return m