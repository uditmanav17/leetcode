class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_idx = 0
        stack = deque([])
        
        for ele in pushed:
            stack.append(ele)
            
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
                
        # return pop_idx == len(popped)
        return not stack

