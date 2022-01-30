
class Solution:
    def trap(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        water = 0

        leftIdx, rightIdx = 0, len(arr) - 1
        leftMax, rightMax = arr[leftIdx], arr[rightIdx]

        while leftIdx < rightIdx:
            if arr[leftIdx] < arr[rightIdx]:
                leftIdx += 1
                leftMax = max(leftMax, arr[leftIdx])
                water += leftMax - arr[leftIdx]
            else:
                rightIdx -= 1
                rightMax = max(rightMax, arr[rightIdx])
                water += rightMax - arr[rightIdx]

        return water

