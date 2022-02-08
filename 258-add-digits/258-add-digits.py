class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num, r = divmod(num, 10)
            num += r
        return num
        