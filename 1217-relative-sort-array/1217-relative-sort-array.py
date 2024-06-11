class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l1=[]
        l2=[]
        for i in arr1:
            if i not in arr2:
                l2.append(i)
            else:
                l1.append(i)
        arr_map={val: idx for idx, val in enumerate(arr2)}
        l1.sort(key = lambda x: arr_map[x])
        l2.sort()
        return l1+l2