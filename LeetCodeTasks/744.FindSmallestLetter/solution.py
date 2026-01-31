from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target: return char
        return letters[0]


if __name__ == '__main__':
    print(Solution().nextGreatestLetter(["c","f","j"], 'a'))