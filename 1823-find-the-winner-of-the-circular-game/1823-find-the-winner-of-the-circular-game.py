# https://leetcode.com/problems/find-the-winner-of-the-circular-game/discuss/1152705/JavaC%2B%2BPython-4-lines-O(n)-time-O(1)-space

# check notes

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        
        for idx in range(1, n+1):
            winner = (winner + k) % idx
            
        return winner + 1