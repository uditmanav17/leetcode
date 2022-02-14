class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        source, target = 0, len(graph) - 1
        
        q = deque([[0]])
        
        while q:
            curr_path = q.popleft()
            last_node = curr_path[-1]
            
            if last_node == target:
                ans.append(curr_path[:])
                
            for node in graph[last_node]:
                q.append(curr_path + [node])
                
        return ans
        
        
        