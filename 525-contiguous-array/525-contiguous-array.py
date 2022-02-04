class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = count = 0
        maps = {}

        for idx, ele in enumerate(nums):
            count += 1 if ele else -1 

            # if we encounter 0, maxLen will be from starting idx
            # as at the beginning count was 0
            if count == 0:
                maxLen = max(maxLen, idx+1)

            # if already seen the count, update maxLen
            if count in maps.keys():
                maxLen = max(maxLen, idx-maps.get(count))
            else:
                maps[count] = idx

        return maxLen

