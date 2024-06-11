class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=[0] * (max(arr1)+1)
        for i in arr1:
            count[i]+=1
        res=[]
        for i in arr2:
            while count[i]>0:
                res.append(i)
                count[i]-=1
        for i in range(max(arr1)+1):
            while count[i]>0:
                res.append(i)
                count[i]-=1
        return res