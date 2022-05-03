class Solution:
    
    def findUnsortedSubarray(self, array: List[int]) -> int:
        
        def is_out_of_order(idx, arr):
            if idx == 0:
                return not arr[idx] <= arr[idx + 1]
            if idx == len(arr) - 1:
                return not arr[idx - 1] <= arr[idx]
            return not arr[idx - 1] <= arr[idx] <= arr[idx + 1]


        if len(array) == 1:
            return 0
        min_out, max_out = float("inf"), float("-inf")

        for idx, num in enumerate(array):
            if is_out_of_order(idx, array):
                min_out = min(min_out, num)
                max_out = max(max_out, num)

        # print(min_out, max_out)
        if min_out == float("inf") and max_out == float("-inf"):
            return 0

        left, right = 0, len(array) - 1
        while min_out >= array[left]:
            left += 1

        while max_out <= array[right]:
            right -= 1


        return right - left + 1

