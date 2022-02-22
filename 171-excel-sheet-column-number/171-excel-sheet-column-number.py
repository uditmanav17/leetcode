class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # number system with base 26 to decimal
        cell = 0
        base = 26
        
        for char in columnTitle:
            cell *= base
            cell += (ord(char) - ord("A") + 1)
            
        return cell
        