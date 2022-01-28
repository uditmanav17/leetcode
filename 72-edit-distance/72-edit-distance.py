
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.dp_sol(word1, word2)
        memo = {}
        return self.memo_sol(word1, word2, 0, 0, memo)
    
    def dp_sol(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dist = [[0] * (l1 + 1) for _ in range(l2 + 1)]

        for r, c in product(range(l2 + 1), range(l1 + 1)):
            if r == 0 or c == 0:
                dist[r][c] = r or c
                continue

            char1 = word2[r - 1]
            char2 = word1[c - 1]

            if char1 == char2:
                dist[r][c] = dist[r - 1][c - 1]
            else:
                dist[r][c] = 1 + min(dist[r - 1][c], 
                                     dist[r][c - 1], 
                                     dist[r - 1][c - 1])

        # pprint(dist)
        return dist[-1][-1]

    
    def memo_sol(self, word1, word2, i, j, memo):
        """Memoized solution"""
        if i == len(word1) and j == len(word2):
            return 0
        
        if i == len(word1):
            return len(word2) - j
        
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.memo_sol(word1, word2, i + 1, j + 1, memo)
            else: 
                insert = 1 + self.memo_sol(word1, word2, i, j + 1, memo)
                delete = 1 + self.memo_sol(word1, word2, i + 1, j, memo)
                replace = 1 + self.memo_sol(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]
    