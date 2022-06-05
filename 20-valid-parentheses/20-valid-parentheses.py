class Solution:
    def isValid(self, s: str) -> bool:
        bkt_map = {"}":"{", ")":"(", "]":"["}
        stk = deque()
        
        for bkt in s:
            if bkt in bkt_map.keys():
                if not stk or stk.pop() != bkt_map[bkt]:
                    return False
            else:
                stk.append(bkt)
                
        return not stk
        