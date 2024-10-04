class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res=0
        leftheap=costs[:candidates]
        rightheap=costs[max(candidates, len(costs)-candidates):]
        heapq.heapify(leftheap)
        heapq.heapify(rightheap)
        leftindex=candidates
        rightindex=max(candidates, len(costs)-candidates)-1
        for i in range(k):
            if not rightheap or (leftheap and leftheap[0]<=rightheap[0]):
                res+=heapq.heappop(leftheap)
                if leftindex<=rightindex:
                    heapq.heappush(leftheap,costs[leftindex])
                    leftindex+=1
            else:
                res+=heapq.heappop(rightheap)
                if leftindex<=rightindex:
                    heapq.heappush(rightheap,costs[rightindex])
                    rightindex-=1
        return res

        