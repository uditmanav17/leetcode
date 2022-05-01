class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = "0" * (len(number) - 1)
        
        for idx, num in enumerate(number):
            if num == digit:
                max_num = max(max_num, number[:idx] + number[idx + 1:])
        return max_num
        