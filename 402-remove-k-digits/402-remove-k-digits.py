class Solution:
    def approach1(self, num: str, k: int) -> str:
        # Time - O(k*n)
        # Space - O(n)
        # remove first peaks, as long as we can remove digits
        num = list("0" + num + "0")
        while k:
            k -= 1
            for idx in range(1, len(num) - 1):
                # print(idx, num)
                if num[idx-1] <= num[idx] > num[idx+1]:
                    num.pop(idx)
                    break
        
        # print(num)
        ans = "".join(num[:-1]).lstrip("0")
        return ans if ans != "" else "0"
        
        
    def approach2(self, num: str, k: int) -> str:
        # Time - O(n)
        # Space - O(n)
        stack = []
        
        for digit in num + "0":
            # directly comparing strings based on ASCII
            # as long as topmost digit of stack is greater than curr digit
            # and we have k > 0, remove topmost digits
            while stack and stack[-1] > digit and k > 0:
                k -= 1
                stack.pop()
            stack.append(digit)
            
        # print(stack)
        # remove leading 0s
        ans = "".join(stack[:-1]).lstrip("0")
        return ans if ans != "" else "0"

        
    def removeKdigits(self, num: str, k: int) -> str:
        # return self.approach1(num, k)
        return self.approach2(num, k)
        
        
        




        