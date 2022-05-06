class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque([("$", 0)])
        
        for char in s:
            last_char, last_char_count = stack[-1]
            
            if last_char == char:
                curr_count = last_char_count + 1
                if curr_count >= k:
                    while (curr_count - 1) > 0:
                        curr_count -= 1
                        stack.pop()
                else:
                    stack.append((char, curr_count))
            else:
                stack.append((char, 1))
                
        # print(stack)
        
        return "".join(char for char, _ in stack)[1:]
                    
        