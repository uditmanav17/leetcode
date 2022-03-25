class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # move all to one city a
        total = sum(a for a, b in costs)
        
        # diff in costs to move to another city b
        refund = sorted([b - a for a, b in costs])
        
        # select min top, which could be negative, 
        # and add them to total as refund
        total += sum(refund[:len(costs)//2])
        
        return total
