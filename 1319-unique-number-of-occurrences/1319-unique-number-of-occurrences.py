class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s={}
        for i in arr:
            s[i]=0
        for i in arr:
            s[i]+=1
        l=[]
        for i in s.values():
            print(i)
            if i in l:
                return False
            else:
                l.append(i)
        return True