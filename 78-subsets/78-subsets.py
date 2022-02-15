class Solution:
    def subset_iterative(self, nums):
        subsets = [[]]
        
        for ele in nums:
            for idx in range(len(subsets)):
                sub = subsets[idx]
                subsets.append(sub.copy() + [ele])
                
        return subsets
    
    
    def subset_bitManipulation(self, nums):
        n = len(nums)
        total_subsets = (1 << n)  # this is 2 ^ n
        subsets = [[] for _ in range(total_subsets)]
        
        for i in range(total_subsets):
            for j in range(n):
                if ((i >> j) & 1):
                    subsets[i].append(nums[j])
                    
        return subsets
        
    
    def subset_recursive(self, nums, start=0, curr_subset=None, subsets=None):
        if subsets is None:
            subsets = []
            
        if curr_subset is None:
            curr_subset = []
            
        subsets.append(curr_subset[:])
        for i in range(start, len(nums)):
            curr_subset.append(nums[i])
            self.subset_recursive(nums, i + 1, curr_subset, subsets)
            curr_subset.pop()
            
        return subsets
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subset_iterative(nums)
        # return self.subset_bitManipulation(nums)
        # return self.subset_recursive(nums)
        
    
        