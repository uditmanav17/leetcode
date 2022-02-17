class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def helper(open_bkt, close_bkt, curr_seq):
            if open_bkt == close_bkt == n:
                result.append("".join(curr_seq))
                return 
            
            if open_bkt < n:
                helper(open_bkt + 1, close_bkt, curr_seq + ["("])
                
            if close_bkt < open_bkt:
                helper(open_bkt, close_bkt + 1, curr_seq + [")"])
                
        helper(0, 0, [])
        
        return result
                
                