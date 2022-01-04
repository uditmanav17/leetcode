# Intuition:
# Consider trust as a graph, all pairs are directed edge.
# The point with in-degree - out-degree = N - 1 become the judge.

# Explanation:
# Count the degree, and check at the end.

# Time Complexity:
# Time O(T + N), space O(N)


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
            
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        
        # print(count)
        return -1
            
            
            
            
        