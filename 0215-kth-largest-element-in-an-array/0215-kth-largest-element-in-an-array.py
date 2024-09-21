class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap=[]
        # for i in nums:
        #     heapq.heappush(heap,i)
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # return heap[0]
        def quick(nums,k):
            pivot=random.choice(nums)
            left,mid,right=[],[],[]
            for i in nums:
                if i<pivot:
                    left.append(i)
                elif i>pivot:
                    right.append(i)
                else:
                    mid.append(i)
            if len(right)>=k:
                return quick(right,k)
            elif (len(mid)+len(right))>=k:
                return pivot
            else:
                return quick(left,k-len(mid)-len(right))
        return quick(nums,k)