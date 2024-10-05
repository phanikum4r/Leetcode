class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        arr=[]
        def findsubsets(arr,index, cur):
            if len(arr)>k or cur>n:
                return
            if cur==n and len(arr)==k:
                res.append(arr[:])
            for val in range(index,10):
                arr.append(val)
                findsubsets(arr,val+1,cur+val)
                arr.pop()
        findsubsets(arr,1,0)
        return res