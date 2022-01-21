# start city will be one in which we enter with min gas

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        total_curr_gas = 0
        start_idx = -1
        min_gas_level = float("inf")
        
        for idx, (curr_gas, curr_cost) in enumerate(zip(gas, cost)):
            if total_curr_gas < min_gas_level:
                min_gas_level = total_curr_gas
                start_idx = idx
            total_curr_gas += (curr_gas - curr_cost)
                
        return start_idx

