class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr=[(nums1[i],nums2[i]) for i in range(len(nums1))]
        arr.sort(key=lambda x:x[1], reverse=True)
        heap=[arr[i][0] for i in range(k)]
        heapq.heapify(heap)
        topsum=sum(heap)
        res=topsum*arr[k-1][1]
        for i in range(k,len(nums1)):
            if arr[i][0]<=heap[0]:
                continue
            topsum-=heapq.heapreplace(heap,arr[i][0])
            topsum+=arr[i][0]
            res=max(topsum*arr[i][1],res)
        return res