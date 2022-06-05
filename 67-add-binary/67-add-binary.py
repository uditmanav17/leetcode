
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        idx1 = idx2 = carry = 0
        ans = []
        
        while idx1 < len(a) or idx2 < len(b) or carry:
            n1 = int(a[idx1]) if idx1 < len(a) else 0
            n2 = int(b[idx2]) if idx2 < len(b) else 0
            
            carry, curr_bit = divmod(n1 + n2 + carry, 2)
            ans.append(curr_bit)
            
            idx1 += 1
            idx2 += 1
                        
        return "".join(map(str, ans[::-1]))
            
            
        