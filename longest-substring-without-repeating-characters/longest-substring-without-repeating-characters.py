class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start_idx = 0
        answer = [0, 0]
        
        for idx, char in enumerate(s):
            if char in last_seen:
                # take example of 'clementisacap' at second 'c' and dry run
                start_idx = max(start_idx, last_seen[char] + 1)
                
            if (answer[1] - answer[0]) < (idx + 1 - start_idx):
                answer = [start_idx, idx + 1]
                
            last_seen[char] = idx
            
        return answer[1] - answer[0]
                
                
                
        
        
        