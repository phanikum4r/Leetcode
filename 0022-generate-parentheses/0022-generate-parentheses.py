class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(arr, left, right):
                if left < n:
                    arr.append('(')
                    backtrack(arr, left+1, right)
                    arr.pop()
                if right < left:
                    arr.append(')')
                    if len(arr)==2*n:
                        result.append("".join(arr))
                    else:
                        backtrack(arr, left, right+1)
                    arr.pop()
        backtrack([],0,0)
        return result

                    
                    