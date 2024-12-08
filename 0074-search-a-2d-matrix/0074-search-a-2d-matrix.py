class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        while top <= bottom:
            mid = (top + bottom)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left, right = 0, len(matrix[mid])-1
                while left <= right:
                    center = (left + right)//2
                    if matrix[mid][center] == target:
                        return True
                    elif matrix[mid][center] < target:
                        left = center + 1
                    else:
                        right = center - 1
            if matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        return False