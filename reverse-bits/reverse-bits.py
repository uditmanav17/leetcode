class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []
        while n:
            n, r = divmod(n, 2)
            ans.append(r)
        s = "".join(str(i) for i in ans)
        s += '0'*(32-len(s))
        return int(s, 2)
        