class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in ratings]

        # travrse l 2 r
        for idx in range(1, len(ratings)):
            if ratings[idx] > ratings[idx - 1]:
                candies[idx] = candies[idx - 1] + 1

        # traverse r 2 l
        for idx in reversed(range(len(ratings) - 1)):
            if ratings[idx + 1] < ratings[idx]:
                candies[idx] = max(candies[idx], candies[idx + 1] + 1)

        # print(candies)
        return sum(candies)



