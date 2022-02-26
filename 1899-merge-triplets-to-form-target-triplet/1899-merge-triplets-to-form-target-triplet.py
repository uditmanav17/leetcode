class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        ans = [0, 0, 0]
        for idx, (x, y, z) in enumerate(triplets):
            if x <= target[0] and y <= target[1] and z <= target[2]:
                ans = [max(ans[0], x), max(ans[1], y), max(ans[2], z)]
                
        # print(ans)
        return ans == target
