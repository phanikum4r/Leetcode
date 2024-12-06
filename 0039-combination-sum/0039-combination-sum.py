class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(arr, start, cur_sum, target_sum):
            for i in range(start, len(candidates)):
                if cur_sum+candidates[i] > target_sum:
                    return
                arr.append(candidates[i])
                cur_sum += candidates[i]
                if cur_sum == target_sum:
                    result.append(arr[:])
                elif cur_sum < target_sum:
                    backtrack(arr,i, cur_sum,target_sum)
                cur_sum-=arr.pop()
        backtrack([],0,0 , target)
        return result