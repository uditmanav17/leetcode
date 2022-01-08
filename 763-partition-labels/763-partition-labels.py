# Compute interval (start, end) for each letter [a-z], 
# where start is first occurrence of letter, and end is last occurrence of letter. 
# Then we merge any overlapping intervals, 
# and the resulting intervals can form the answer.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        
        for idx in range(1, len(intervals)):
            currStart, currEnd = intervals[idx]
            oldStart, oldEnd = ans[-1]
            if currStart <= oldEnd:
                ans[-1] = [oldStart, max(currEnd, oldEnd)]
            else:
                ans.append([currStart, currEnd])
        
        return ans
    
    def partitionLabels(self, s: str) -> List[int]:
        # get (start, end) for each char
        maps = {}
        for idx, char in enumerate(s):
            if char in maps:
                new_interval = maps.get(char)
                new_interval[1] = idx
                maps[char] = new_interval
            else:
                maps[char] = [idx, idx]
                
        # print(maps)
        intervals = [v for k, v in maps.items()]
        merged_intervals = self.merge(intervals)
        # print(merged_intervals)
        
        return [(j - i + 1) for i, j in merged_intervals]
        
        
        