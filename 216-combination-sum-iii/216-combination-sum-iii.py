class Solution:
    def helper(self, arr, start_idx, k, n, curr_nums, all_combinations):
        curr_total = sum(curr_nums)
        curr_total_len = len(curr_nums)
        
        if curr_total_len == k and curr_total == n:
            all_combinations.append(curr_nums[:])
            return 
        
        if curr_total_len > k or curr_total > n:
            return
        
        for idx in range(start_idx, len(arr)):
            num = arr[idx]
            new_total = curr_total + num
            if new_total <= n:
                self.helper(arr, idx + 1, 
                            k, n, 
                            curr_nums + [num], 
                            all_combinations)


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = list(range(1, 10))
        ans = []
        self.helper(arr, 0, k, n, [], ans)
        # print(ans)
        return ans
        