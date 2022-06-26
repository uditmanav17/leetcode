class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n, total = len(arr), sum(arr)
        best = running_sum = sum(arr[:n - k])
        
        for idx in range(n - k, n):
            running_sum += (arr[idx] - arr[idx - n + k])
            best = min(best, running_sum)
            
        return total - best
