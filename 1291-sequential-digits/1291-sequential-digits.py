class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # all digits required for number creation
        q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
        ans = []

        while q:
            # print(q)
            curr_num = q.popleft()
            if low <= curr_num <= high:
                ans.append(curr_num)

            last_digit = curr_num % 10
            if last_digit < 9:
                # create next_num and add to q
                next_num = curr_num * 10 + (last_digit + 1)
                if next_num > high:
                    continue
                q.append(next_num)

        return ans

