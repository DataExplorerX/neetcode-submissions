class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        start = 0
        current_tank = 0

        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        
        return start

        