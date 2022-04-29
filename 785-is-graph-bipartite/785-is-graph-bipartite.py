class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes = len(graph)
        colored = {}
        
        for curr_node in range(nodes):
            if curr_node not in colored and graph[curr_node]:
                colored[curr_node] = 1
                
                q = deque([curr_node])
                while q:
                    cur = q.popleft()
                    
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            q.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
                    
        return True
                    
                    
                
                
            