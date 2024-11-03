class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom , left , right = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while top<=bottom and left<=right:
            
            for j in range(left, right+1):
                result.append(matrix[top][j])
            top += 1

            for j in range(top, bottom+1):
                result.append(matrix[j][right])
            right -= 1

            if top>bottom or left>right:
                break

            for j in range(right, left-1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

            for j in range(bottom, top-1, -1):
                result.append(matrix[j][left])
            left += 1

        return result