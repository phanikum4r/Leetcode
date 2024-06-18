class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        answer=[]
        for i in nums:
            answer.append(p)
            p*=i
        p=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=p
            p*=nums[i]
        return answer