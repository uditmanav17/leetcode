class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
		# we work with positive numbers only and worry about the sign in the end
        positiveSign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        for i in reversed(range(dividend.bit_length() - divisor.bit_length() + 1)):
            if divisor <= (dividend >> i):
                dividend -= divisor << i
                quotient |= 1 << i
        
		# min handles corner case -2 ** 31 / -1 = 2 ** 31
        return min(2 ** 31 - 1, quotient) if positiveSign else -quotient
