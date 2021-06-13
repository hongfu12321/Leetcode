class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Iterate throught the station and find every posible start station
        # From the start station, check one by one to see if it is availibe
        if sum(gas) - sum(cost) < 0: return -1
            
        n, tank, start = len(gas), 0, 0        
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
                
        return start