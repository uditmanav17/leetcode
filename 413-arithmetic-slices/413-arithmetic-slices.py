
"""
Every digit that gets added to the sequence, adds 'n' more possibilities to the output where 'n' is the difference between number of digits in array and 3.

e.g For [1,2,3] we have [1,2,3]
For [1,2,3,4] we have [1,2,3], [1,2,3,4], [2,3,4] ie it adds 2 new sub-arrays ending with 4.
For [1,2,3,4,5], we have [1,2,3,4,5], [2,3,4,5], [3,4,5] ie it adds 3 new sub-arrays ending with 5 to whatever we could make with 4 elements ie [1,2,3,4]
Likewise for 6 elements, we will have 4 new sub-arrays that'd be added, so on and forth.

TLDR:

So the logic is to add 1 to every single element that gets added in the sequence.

"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_seqs = curr_seqs = 0
        
        if len(nums) < 3:
            return 0
        
        for idx in range(1, len(nums) - 1):
            prev, curr, next_ = nums[idx-1], nums[idx], nums[idx+1]
            if (next_ - curr) == (curr - prev):
                # print(idx, curr_seqs)
                curr_seqs += 1
                total_seqs += curr_seqs
            else:
                curr_seqs = 0
                
        return total_seqs
        
        
        
        