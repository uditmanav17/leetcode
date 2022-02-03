class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], 
                     nums3: List[int], nums4: List[int]) -> int:
        
        ans = 0
        totals_1 = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                curr_sum = nums1[i] + nums2[j]
                totals_1[curr_sum] = totals_1.get(curr_sum, 0) + 1
                
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                curr_sum = -(nums3[i] + nums4[j])
                if curr_sum in totals_1:
                    ans += totals_1.get(curr_sum)
                
        return ans
    