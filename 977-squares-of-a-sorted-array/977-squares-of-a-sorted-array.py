class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        answer = [0] * len(nums)
        
        idx = r
        while l <= r:
            n1 = abs(nums[l])
            n2 = abs(nums[r])
            if n1 > n2:
                l += 1
                max_num = n1
            else:
                r -= 1
                max_num = n2
            answer[idx] = max_num ** 2
            idx -= 1
            
        return answer
                
            
        