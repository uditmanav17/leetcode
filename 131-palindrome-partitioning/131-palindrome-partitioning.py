class Solution:
    def is_palindrome(self, s:str):
        return s == s[::-1]
    
    def palindromeHelper(self, s:str, startIdx:int, curr_str: list, 
                         result: list, palindromes: set):
        if len("".join(curr_str)) == len(s):
            result.append(curr_str[:])
        else:
            for cut_point in range(startIdx, len(s)):
                new_str = s[startIdx:cut_point+1]
                # print(new_str)
                if new_str in palindromes or self.is_palindrome(new_str):
                    curr_str.append(new_str)
                    palindromes.add(new_str)
                    self.palindromeHelper(s, cut_point + 1, curr_str, result, palindromes)
                    curr_str.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.palindromeHelper(s, 0, [], result, set())
        # print(result)
        return result
        
        
        