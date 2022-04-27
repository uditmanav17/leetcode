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
        if xr != yr:
            self.p[yr] = xr


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DSU(len(s))
        
        # Grouping
        for x, y in pairs:
            if dsu.find(x) == dsu.find(y): 
                continue
            dsu.union(x, y)
        # print(dsu.p)
        
        
        dic = defaultdict(list)
        for idx, el in enumerate(dsu.p):
            dic[dsu.find(el)].append(idx)
        # print(dic)
        # eg. pairs = [[0,3],[1,2]], dic = {0: [0, 3], 1: [1, 2]}
        
        # sorting 
        ans = list(s)
        for k, idx_list in dic.items():
            char_list = [s[i] for i in idx_list]
            char_list.sort()
            
            # print(idx_list, char_list)
            
            # eg. idx_list = [0, 3], char_list = [b, d]
            # for loop below, idx = [0, b], char = [3, d]
            for idx, char in zip(idx_list, char_list):
                ans[idx] = char
            # print(ans)
            
        return "".join(ans)
        
            
        