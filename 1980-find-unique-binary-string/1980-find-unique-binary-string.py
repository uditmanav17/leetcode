# https://leetcode.com/problems/find-unique-binary-string/discuss/1418687/Detailed-Explanation-O(N)-short-concise-code-Cantor's-Diagonalization-Java-Python-C%2B%2B

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            res.append(str(1 - int(nums[i][i])))
        return "".join(res)
