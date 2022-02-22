class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)

        @lru_cache(None)
        def word_break_helper(start_idx):
            if start_idx == n:
                return True

            for idx in range(n):
                curr_word = s[start_idx : idx + 1]
                if curr_word in wordDict and word_break_helper(idx + 1):
                    return True

            return False

        return word_break_helper(0)

