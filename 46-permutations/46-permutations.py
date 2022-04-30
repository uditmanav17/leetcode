class Solution:
    
    @staticmethod
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    
    def helper(self, start_idx, arr, ans):
        if start_idx == len(arr) - 1:
            ans.append(arr[:])
        else:
            for idx in range(start_idx, len(arr)):
                self.swap(arr, idx, start_idx)
                self.helper(start_idx + 1, arr, ans)
                self.swap(arr, idx, start_idx)
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_perms = []
        self.helper(0, nums, all_perms)
        return all_perms
