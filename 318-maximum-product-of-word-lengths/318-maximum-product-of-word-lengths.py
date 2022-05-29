class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d, ans = defaultdict(int), 0
        
        for word in words:
            for char in word:
                d[word] |= 1 << (ord(char) - 97)
                
        # print(d)
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
                
        return ans 
        