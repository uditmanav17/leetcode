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
        
        
        ans = deque(list(self.numpad[digits[0]])) if digits else []
        
        for digit in digits[1:]:
            curr_ans_len = len(ans)
            for _ in range(curr_ans_len):
                curr_seq = ans.popleft()
                new_seq = [curr_seq + char for char in self.numpad[digit]]
                ans.extend(new_seq)
        
        return ans
