class Solution:
        
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = Counter(arr)
        
        ans, M = 0, 10**9 + 7
        
        # all numbers are different
        for i, j in permutations(c, 2):
            if i < j < target - i - j:
                ans += c[i] * c[j] * c[target - i - j]    
            # print(i, j, target - i - j)
            

        for num in c:
            # all nums same
            if 3 * num == target:
                ans += c[num] * (c[num] - 1) * (c[num] - 2) // 6
            else:
                # 2 same, 1 diff
                ans += c[num] * (c[num] - 1) * (c[target - 2 * num]) // 2
                
        return ans % M

