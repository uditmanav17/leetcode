
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(None)
        def dfs(num):
            # if no moves available, player loses
            if num == 0:
                return False
            
            # starting from some stones, 
            # try removing these number of stones to reach a state from which alice can win
            for curr_num in reversed(range(1, int(sqrt(num)) + 1)):
                if not dfs(num - curr_num**2):
                    return True
                
            return False
        
        return dfs(n)
        