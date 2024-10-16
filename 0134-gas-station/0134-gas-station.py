class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gain, total_gain, start = 0, 0, 0
        for i in range(len(gas)):
            cur_gain += gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            if cur_gain < 0:
                cur_gain = 0
                start = i + 1
        return start if total_gain >= 0 else -1