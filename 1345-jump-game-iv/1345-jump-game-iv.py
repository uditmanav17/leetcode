# https://leetcode.com/problems/jump-game-iv/discuss/988714/Python-bfs-with-small-trick-explained
# https://leetcode.com/problems/jump-game-iv/discuss/1690813/Best-explanation-EVER-possible-for-this-question

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dest = len(arr) - 1
        
        graph = defaultdict(list)
        for idx, num in enumerate(arr):
            graph[num].append(idx)
            
        q = deque([(0, 0)])  # (steps, idx)
        visited_idx = set()
        
        while q:
            steps, idx = q.popleft()
            curr_val = arr[idx]
            if idx == dest:
                return steps
            
            visited_idx.add(idx)
            for nieghbour_idx in (idx - 1, idx + 1):
                if 0 <= nieghbour_idx <= dest and nieghbour_idx not in visited_idx:
                    q.append((steps + 1, nieghbour_idx))
                    
            for jump_idx in graph[curr_val]:
                if jump_idx not in visited_idx:
                    q.append((steps + 1, jump_idx))
                    
            # needed to clear one of test case
            graph[curr_val].clear()
                    
            
            
        