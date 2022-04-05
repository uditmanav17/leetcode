
class Solution:
    def maxArea(self, arr) -> int:
        if len(arr) == 0:
            return 0

        maxwater = 0
        
        left, right = 0, len(arr) - 1
        leftMax, rightMax = arr[left], arr[right]

        while left < right:
            diff = right - left
            water = min(leftMax, rightMax) * diff
            maxwater = max(maxwater, water)
            
            if arr[left] < arr[right]:
                left += 1
                leftMax = max(leftMax, arr[left])
            else:
                right -= 1
                rightMax = max(rightMax, arr[right])

        return maxwater

