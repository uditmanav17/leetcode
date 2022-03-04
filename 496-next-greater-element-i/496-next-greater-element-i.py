class Solution:
    def get_next_grtr(self, nums):
        stack = deque([])
        nums_grtr = {}
        
        for idx, ele in enumerate(nums):
            # print(ele, stack, nums_grtr)
            while stack and ele > nums[stack[-1]]:
                curr_idx = stack.pop()
                nums_grtr[nums[curr_idx]] = ele
                
            if not stack or ele < nums[stack[-1]]:
                stack.append(idx)

        # print(nums_grtr)
        return nums_grtr


    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        nums2_grtr = self.get_next_grtr(nums2)
        
        return [nums2_grtr.get(ele, -1) for ele in nums1]
        
        