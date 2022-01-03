class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        answer = set()
        
        for idx in range(len(s) - 10 + 1):
            curr_seq = s[idx : idx + 10]
            if curr_seq in seen:
                answer.add(curr_seq)
            seen.add(curr_seq)
        
        return list(answer)
                
            
        