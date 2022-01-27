class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0

        for i in reversed(range(32)):
            mask |= 1 << i
            # print(i, mask, bin(mask))

            found = set([num & mask for num in nums])
            # print(f"{found = }")

            start = ans | 1 << i
            # print(f"{start = }, {ans = }")
            # print(f"{bin(start) = }, {bin(ans) = }")

            for pref in found:
                # print(f"{pref} {start ^ pref} {bin(pref)}")
                if start ^ pref in found:
                    ans = start
                    break
            # print()

        return ans

        