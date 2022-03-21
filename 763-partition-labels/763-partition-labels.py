class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {char:idx for idx, char in enumerate(s)}
        
        ans = [-1]
        
        covered_idx = 0
        for idx, char in enumerate(s):
            covered_idx = max(covered_idx, last_seen[char])
            
            if covered_idx == idx:
                ans.append(covered_idx)
        
        return [ans[idx] - ans[idx - 1] for idx in range(1, len(ans))]
        