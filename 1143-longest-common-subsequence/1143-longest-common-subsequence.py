class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)

        lcs = [[0] * (l1+1) for _ in range(l2+1)]

        for idx1 in range(1, l2+1):
            for idx2 in range(1, l1+1):
                if s2[idx1-1] == s1[idx2-1]:
                    lcs[idx1][idx2] = lcs[idx1-1][idx2-1] + 1 
                else:
                    lcs[idx1][idx2] = max(lcs[idx1-1][idx2], lcs[idx1][idx2-1])
        return lcs[-1][-1]
