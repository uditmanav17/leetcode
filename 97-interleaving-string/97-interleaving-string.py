from pprint import pprint as pp

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1)+len(s2)):
            return False
        
        n1 = len(s1) + 1
        n2 = len(s2) + 1
        
        cache = [[False for _ in range(n2)] for _ in range(n1)]

        for i, j in product(range(n1), range(n2)):
            k = i + j

            if i == 0 and j == 0:
                cache[i][j] = True

            elif i == 0:
                cache[i][j] = cache[i][j-1] and s2[j-1]==s3[k-1]

            elif j == 0:
                cache[i][j] = cache[i-1][j] and s1[i-1]==s3[k-1]

            else:
                condition1 = cache[i][j-1] and s2[j-1]==s3[k-1]
                condition2 = cache[i-1][j] and s1[i-1]==s3[k-1]
                cache[i][j] = condition1 or condition2

        # pp(cache)
        return cache[-1][-1]
