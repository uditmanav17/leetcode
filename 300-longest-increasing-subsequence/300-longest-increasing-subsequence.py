class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        piles = []
        
        for num in nums:
            if not piles:
                piles.append([num])
                
            else:
                added = False
                for pile in piles:
                    n2 = pile[-1]
                    if n2 >= num:
                        pile.append(num)
                        added = True
                        break
                if not added:
                    piles.append([num])
                    
        # print(piles)
        return len(piles)
                    
        
        