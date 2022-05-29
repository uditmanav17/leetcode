class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = deque([])
        last = float("-inf")
        
        for num in nums[::-1]:
            if last > num:
                return True
            
            while stack and stack[-1] < num:
                last = stack.pop()
                
            stack.append(num)
                
        return False
                
            
        