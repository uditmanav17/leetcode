

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # nodes with 0 in degree
        nodes_indegree = [0] * n
        
        for from_, to_ in edges:
            nodes_indegree[to_] += 1
            
        answer = []
        for idx, indegee in enumerate(nodes_indegree):
            if indegee == 0:
                answer.append(idx)
            
        return answer
        