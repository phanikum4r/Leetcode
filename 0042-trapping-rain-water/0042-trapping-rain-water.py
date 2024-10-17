class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        cur_vol=0
        for i in range(len(height)):
            while stack and height[stack[-1]]<=height[i]:
                left = stack.pop()
                if not stack:
                    break
                cur_vol += (min(height[i], height[stack[-1]])-height[left])*(i-stack[-1]-1) 
            stack.append(i)
        return cur_vol
