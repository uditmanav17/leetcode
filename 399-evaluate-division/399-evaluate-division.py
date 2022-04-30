class Solution:
    def calcEquation(self, 
                     equations: List[List[str]], 
                     values: List[float], 
                     queries: List[List[str]]) -> List[float]:
        
        def build_graph(eqn, values):
            graph = {}
            for (to_, from_), val in zip(eqn, values):
                graph.setdefault(to_, [])
                graph[to_].append((from_, val))
                
                graph.setdefault(from_, [])
                graph[from_].append((to_, 1/val))
            
            return graph
        
        def solve_query(graph, source, dest):
            src = graph.get(source)
            des = graph.get(dest)
            if src is None or des is None:
                return -1
            if source == dest:
                return 1
            
            q = deque(graph[source])
            visited = set([source])
            
            while q:
                # print(q, visited)
                node, dist = q.popleft()
                if node == dest: return dist
                if node in visited: continue
                
                visited.add(node)
                neighbors = deque(graph[node])
                
                while neighbors:
                    n, d = neighbors.popleft()
                    if n in visited:
                        continue
                    q.append((n, dist * d))
            
            return -1
                
        
        graph = build_graph(equations, values)
        # print(graph)
        ans = [solve_query(graph, s, d) for s, d in queries]
        return ans
        
        
                
                
        
        