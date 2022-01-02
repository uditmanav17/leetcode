class Solution:

    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        allPerms = []
        self.permuteHelper(0, nums, allPerms)
        return allPerms

    def permuteHelper(self, idx, arr, allPerms):
        if idx == len(arr) - 1:
            allPerms.append(arr[:])
        else:
            for j in range(idx, len(arr)):
                self.swap(arr, idx, j)
                self.permuteHelper(idx + 1, arr, allPerms)
                self.swap(arr, idx, j)

