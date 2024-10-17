class Solution:
    def trap(self, height: List[int]) -> int:
        # stack=[]
        # cur_vol=0
        # for i in range(len(height)):
        #     while stack and height[stack[-1]]<=height[i]:
        #         left = stack.pop()
        #         if not stack:
        #             break
        #         #subtract the left from height as we added to ans in previous
        #         cur_vol += (min(height[i], height[stack[-1]])-height[left])*(i-stack[-1]-1) 
        #     stack.append(i)
        # return cur_vol

        left_max, right_max = 0, 0
        left, right = 0, len(height)-1
        ans=0
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                ans += right_max - height[right]
                right -=1
        return ans