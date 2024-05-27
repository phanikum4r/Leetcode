class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total=0
        subset=defaultdict(int)
        nums.sort(key=lambda x:(x%k,x))
        for num in nums:
            current_subsets=total + 1 - subset[num-k]
            subset[num] +=current_subsets
            total+= current_subsets
        return total