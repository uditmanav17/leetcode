
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        graph = {idx: l for idx, l in enumerate(isConnected)}
        connected_compo = 0
        
        for node in graph:
            if not visited[node]:
                self.dfs(node, graph, visited)
                connected_compo += 1
        
        return connected_compo


    def dfs(self, node, graph, visited):
        visited[node] = True
        for curr_node, edge in enumerate(graph[node]):
            if not visited[curr_node] and edge == 1:
                self.dfs(curr_node, graph, visited)
        
        
