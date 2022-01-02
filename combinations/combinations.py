class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        elements = list(range(1, n + 1))
        result = []
        self.combineHelper(elements, k, [], result)
        return result

    def combineHelper(self, elements, k, curr_res, result):
        if len(curr_res) == k:
            result.append(curr_res)

        for idx in range(len(elements)):
            self.combineHelper(
                elements[idx + 1 :], k, curr_res + [elements[idx]], result
            )
