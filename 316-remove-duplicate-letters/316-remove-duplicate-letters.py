class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_seen = {}

        for idx, char in enumerate(s):
            last_seen[char] = idx

        stack = deque([])
        seen = {}
        
        for idx, char in enumerate(s):
            # print(idx, char, stack, seen)
            if seen.get(char, False):
                continue

            while stack and stack[-1] > char and last_seen[stack[-1]] > idx:
                seen[stack.pop()] = False

            stack.append(char)
            seen[char] = True

        return "".join(stack)
