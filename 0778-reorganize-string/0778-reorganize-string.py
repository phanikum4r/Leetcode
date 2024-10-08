class Solution:
    def reorganizeString(self, s: str) -> str:
        chars=Counter(s)
        sorted_chars = sorted(chars.items(), key = lambda x: -x[1])
        if sorted_chars[0][1]>(len(s)+1)//2:
            return ""
        res=[""]*len(s)
        idx=0
        for char, count in sorted_chars:
            for _ in range(count):
                res[idx]=char
                idx+=2
                if idx>=len(s):
                    idx=1
        return "".join(res)