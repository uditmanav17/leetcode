https://leetcode.com/problems/divide-two-integers/discuss/2089781/Go-back-to-the-(elementary-school)-basics-or-w-examples
​
https://leetcode.com/problems/divide-two-integers/discuss/1925614/Python-or-Bit-Manipulation-or-Simple-Solution-With-Explanation
​
Logic:
- Since we have to avoid the usage of '/', '%', '*' operators so what we could do is, we could subtract the dividend by double multiplier of divisor until dividend becomes smaller than divisor.
- For example, dividend = 40, divisor = 3
1. Can we take 3 out of 40? Yes! So, dividend => 40-3 = 37, divisor => 3*2 = 6
2. Can we take 6 out of 37? Yes! So, dividend => 37-6 = 31, divisor => 6*2 = 12
3. Can we take 12 out of 31? Yes! So, dividend => 31-12 = 19, divisor => 12*2 = 24
4. Can we take 24 out of 19? No! Now we have to again follow the above approach by resetting the divisor.
So, dividend = 19, divisor = 3 And ans till now is, 1 + 2 + 4 = 7
5. Can we take 3 out of 19? Yes! So, dividend => 19-3 = 16, divisor => 3*2 = 6
6. Can we take 6 out of 16? Yes! So, dividend => 16-6 = 10, divisor => 6*2 = 12
7. Can we take 12 out of 10? No! Now we have to again follow the above approach by resetting the divisor.
So, dividend = 10, divisor = 3 And ans till now is, 7 + 1 + 2 = 10
8. Can we take 3 out of 10? Yes! So, dividend => 10-3 = 7, divisor => 3*2 = 6
9. Can we take 6 out of 7? Yes! So, dividend => 7-6 = 1, divisor => 3*2 = 12
10. Terminate the iterations because dividend < divisor.
And ans till now is, 10 + 1 + 2 = 13
​