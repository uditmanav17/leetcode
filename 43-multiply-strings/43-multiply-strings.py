# https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0] * (len(num1 + num2))
        
        for idx1 in reversed(range(len(num1))):
            for idx2 in reversed(range(len(num2))):
                d1 = ord(num1[idx1]) - ord('0')
                d2 = ord(num2[idx2]) - ord('0')
                
                val = d1 * d2
                ans[idx1 + idx2 + 1] += val
                carry, curr_digit = divmod(ans[idx1 + idx2 + 1], 10)
                # print(val, carry, curr_digit)
                
                ans[idx1 + idx2 + 1] = curr_digit
                ans[idx1 + idx2] += carry
                
                # print(ans)
        ans = "".join(str(i) for i in ans).lstrip('0')
        return ans if ans else '0'