class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i<j:
            x = numbers[i]+numbers[j]
            if target==x:
                return [i+1,j+1]
            elif x>target:
                j-=1
            else:
                i+=1