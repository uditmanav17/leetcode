class Solution:
    def __init__(self):
        self.numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        
        for digit in digits:
            if not ans:
                ans = list(self.numpad[digit])
                continue
                
            temp_q = ans[:]
            q = list(self.numpad[digit])
            ans.clear()
            
            while q:
                ele = q.pop()
                ans.extend([i + ele for i in temp_q])
                
        return ans
                
                
            
                
                
            
        