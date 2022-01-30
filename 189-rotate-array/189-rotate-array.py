class Solution:
    def rev(self, arr, start_idx, end_idx):
        while start_idx < end_idx:
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
            start_idx += 1
            end_idx -= 1
            
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.rev(nums, 0, n - k - 1)
        self.rev(nums, n - k, n - 1)
        self.rev(nums, 0, n - 1)
        
        
        