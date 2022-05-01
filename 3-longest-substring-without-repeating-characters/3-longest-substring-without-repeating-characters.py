class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start_idx = 0
        longest = [0, 0]

        for idx, char in enumerate(s):
            if char in seen:
                start_idx = max(seen[char] + 1, start_idx)

            seen[char] = idx

            curr_len = idx - start_idx + 1
            if curr_len > (longest[1] - longest[0]):
                longest = [start_idx, idx + 1]

        return longest[1] - longest[0]

        