class Solution:
    def addDigits(self, num: int) -> int:
        return self.approach2(num)
        
    def approach1(self, num: int):
        while num > 9:
            num = sum(int(c) for c in str(num))
        return num
        
    # check notes/solution
    def approach2(self, num: int):
        return 0 if num == 0 else (num - 1) % 9 + 1
        