class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(arr, i):
            for num in range(i+1, n+1):
                arr.append(num)
                if len(arr) == k:
                    result.append(arr[:])
                else:
                    backtrack(arr, num)
                arr.pop()
        backtrack([], 0)
        return result