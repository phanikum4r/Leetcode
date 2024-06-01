class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in nums:
            xor^=i
        diffbit =xor & -xor
        n1,n2 = 0,0
        for i in nums:
            if i & diffbit:
                n1^=i
            else:
                n2^=i
        return [n1,n2]