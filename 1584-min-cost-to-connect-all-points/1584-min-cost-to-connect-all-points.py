class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


class Solution:
    def minCostConnectPoints(self, P):
        n, edges = len(P), []
        
        for i in range(n):
            for j in range(i+1, n):
                edges += [(i, j, abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1]))]
                
        dsu, ans = DSU(n), 0
        for x, y, w in sorted(edges, key = lambda x:x[2]):
            if dsu.find(x) == dsu.find(y): continue
            dsu.union(x, y)
            ans += w
            
        return ans
