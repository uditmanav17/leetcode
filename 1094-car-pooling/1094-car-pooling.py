# https://leetcode.com/problems/car-pooling/discuss/857489/Python-linear-solution-using-cumulative-sums-explained
# https://leetcode.com/problems/car-pooling/discuss/1669644/Well-Explained-2-Ways-JAVA-C%2B%2B-PYTHON-Js-oror-Easy-for-mind-to-Accept-it


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        m = max([i for _, _, i in trips])
        times = [0] * (m + 2)

        for i, j, k in trips:
            times[j + 1] += i
            times[k + 1] -= i

        return max(accumulate(times)) <= capacity

