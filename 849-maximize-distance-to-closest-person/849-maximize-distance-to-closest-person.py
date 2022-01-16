
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        n = len(seats)
        left, right = [n] * n, [n] * n
        
        for left_idx in range(n):
            if seats[left_idx] == 1:
                left[left_idx] = 0
            elif left_idx > 0:
                left[left_idx] = left[left_idx-1] + 1
            
            
            right_idx = n - left_idx - 1
            if seats[right_idx] == 1:
                right[right_idx] = 0
            elif right_idx < (n - 1):
                right[right_idx] = right[right_idx+1] + 1
            
            
        # print(left, right)
        ans = [min(left[i], right[i]) for i in range(n)]
        # print(ans)
        
        return max(ans)
            