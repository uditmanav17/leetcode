# https://leetcode.com/problems/word-break/discuss/1455100/Python-2-solutions-(Optimized-with-Trie)-Clean-and-Concise
# try opimization with trie

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        
        @lru_cache(None)
        def dp_recursive(start):
            if start == n:
                return True
            
            for idx in range(start, n):
                curr_word = s[start:idx+1]
                # print(curr_word)
                if curr_word in wordDict and dp_recursive(idx + 1):
                    return True
                
            return False


        return dp_recursive(0)
