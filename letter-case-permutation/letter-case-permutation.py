# https://leetcode.com/problems/letter-case-permutation/discuss/1068063/Python-Honest-backtracking-%2B-oneliner-explained

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        chars = list(s)
        
        def backtrack(i):
            ret.append(''.join(chars))

            for i in range(i, len(chars)):
                if chars[i].isalpha():
                    chars[i] = chars[i].swapcase()
                    backtrack(i+1)
                    chars[i] = chars[i].swapcase() # undo
                
        backtrack(0)
        
        return ret