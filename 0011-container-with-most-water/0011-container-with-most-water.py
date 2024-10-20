class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return area