from typing import List
from collections import deque
from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        seen = set()
        if endWord not in wordListSet:
            return 0

        q = deque([(beginWord, 1)])

        # BFS for every character
        while q:
            curr_word, curr_len = q.popleft()
            if curr_word == endWord:
                return curr_len

            for idx, curr_char in enumerate(curr_word):
                for replace_char in ascii_lowercase:
                    new_word = curr_word[:idx] + replace_char + curr_word[idx + 1 :]
                    if new_word in wordListSet and new_word not in seen:
                        seen.add(new_word)
                        q.append((new_word, curr_len + 1))
            # print(q)
        return 0
