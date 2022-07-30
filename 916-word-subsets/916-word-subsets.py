class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt = Counter()
        for w2 in words2:
            cnt |= Counter(w2)
        # print(cnt)
            
        return [w1 for w1 in words1 if not cnt - Counter(w1)]
