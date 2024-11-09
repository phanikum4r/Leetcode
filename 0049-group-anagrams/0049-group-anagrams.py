class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            t="".join(sorted(i))
            if t in d:
                d[t].append(i)
            else:
                d[t]=[i]
        res=[]
        for i in d:
            res.append(d[i])
        return res