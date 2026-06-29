from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0 

        for curr in patterns:
            if curr in word: counter += 1
        return counter
