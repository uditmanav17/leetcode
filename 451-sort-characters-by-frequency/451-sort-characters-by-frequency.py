from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        arr = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return "".join(char * count for char, count in arr)
        