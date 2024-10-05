class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        arr = []
        res=[]
        letter={"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz",}
        def findsubsets(arr,index):
            if index>=n:
                return
            for val in letter[digits[index]]:
                arr.append(val)
                if index==n-1:
                    res.append("".join(arr))
                findsubsets(arr,index+1)
                arr.pop()
        findsubsets(arr,0)
        return res