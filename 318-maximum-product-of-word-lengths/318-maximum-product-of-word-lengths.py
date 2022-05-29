class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        
        for idx1 in range(len(words)):
            w1 = words[idx1]
            for idx2 in range(idx1):
                w2 = words[idx2]
                intersection = set(w1).intersection(set(w2))
                # print(intersection)
                if len(intersection) == 0:
                    ans = max(ans, len(w1) * len(w2))
                    
        return ans
        