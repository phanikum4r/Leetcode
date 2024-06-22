class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        m,c=0,0
        for i in range(len(seats)):
            if seats[i]==1:
                m=i
                break
        for i in seats:
            if i==0:
                c+=1
                m=max(m,(c+1)//2)
            else:
                c=0
        return max(m,c)