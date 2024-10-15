class Solution:
    def jump(self, nums: List[int]) -> int:
        # res=[len(nums)-1]*len(nums)
        # res[len(nums)-1]=0
        # for i in range(len(nums)-2,-1,-1):
        #     if nums[i]+i>=len(nums)-1:
        #         res[i]=1
        #     elif nums[i]>0:
        #         res[i]=1+min([res[i+j] for j in range(1, nums[i]+1)]) 
        # return res[0]

        far, end, jumps = 0, 0, 0
        for i in range(len(nums)-1):
            far = max(far, nums[i] + i)
            if i == end:
                jumps += 1
                end = far
        return jumps