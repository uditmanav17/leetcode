class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next_num(n):
            ans = 0
            while n:
                n, r = divmod(n, 10)
                ans += r * r
            return ans
        
        if n == 1:
            return True
        
        seen = set([n])
        while n:
            next_num = get_next_num(n)
            if next_num in seen:
                return False
            elif next_num == 1:
                return True
            seen.add(next_num)
            n = next_num
            
            
        return False