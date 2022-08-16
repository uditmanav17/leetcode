class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for idx, char in enumerate(s):
            if counts[char] == 1:
                return idx
        return -1
        