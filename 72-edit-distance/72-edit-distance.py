
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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
