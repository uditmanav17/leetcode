class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseInRange(arr, start_idx, end_idx):
            # start and end are inclusive
            while start_idx <= end_idx:
                arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
                start_idx += 1
                end_idx -= 1
                
        
        n = len(nums)
        k %= n
        cut_point = n - k - 1
        # print(n, k, cut_point)
        reverseInRange(nums, 0, cut_point)
        reverseInRange(nums, cut_point + 1, n - 1)
        reverseInRange(nums, 0, n - 1)
            
        