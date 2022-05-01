class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s= self.vi(S)
        t= self.vi(T)
        print(s, t)
        return self.vi(S) == self.vi(T)
    
    def vi(self, s: str):
        ans = []
        for char in s:
            if char=='#':
                if ans:
                    ans.pop()
            else:
                ans.append(char)
        return "".join(ans)
        