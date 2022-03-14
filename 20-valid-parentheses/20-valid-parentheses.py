class Solution:
    def isValid(self, s: str) -> bool:
        
        maps = {k:v for k, v in zip("]})", "({["[::-1])}
        # print(maps)
        
        stack = deque([])
        
        for char in s:
            if char in maps.keys():
                if not stack or stack.pop() != maps[char]:
                    return False
            else:
                stack.append(char)
        
        # print(stack)
        
        return not stack
            
                
        