class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for hour in range(12):
            h_bits = bin(hour).count("1")
            for minute in range(60):
                m_bits = bin(minute).count("1")
                if h_bits + m_bits == turnedOn:
                    ans.append(f"{hour}:{str(minute).zfill(2)}")
                    
        return ans
                
                
        