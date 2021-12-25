
# https://leetcode.com/problems/longest-palindrome/discuss/791032/Python-2-lines-with-counter-%2B-Oneliner-explained

# all we need to do is to count frequencies of each letter and take as much letters as possible. There are two possible cases:

# (1) If we have only zero or one letters with odd frequencies, then we can use all the letters.
# (2) If we have k>1 letters with odd frequencies, we need to remove exactly k-1 letter to build palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum([freq % 2 for _,freq in Counter(s).items()])
        return len(s) if odds <= 1 else len(s) - odds + 1 
