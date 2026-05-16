class Solution:
    from typing import List
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        slovar = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        result = []
        def backtrack(index: int, current_combination: str):
            if index == len(digits):
                result.append(current_combination)
                return
            current_digit = digits[index]
            letters = slovar[current_digit]
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        backtrack(0, "")
        return result

# Runtime 0 ms, 100 %
# Memory 17.58 mb, 75 %
def main():
    solution = Solution()
    input1, input2 = "23", '2'
    print(solution.letterCombinations(input1))
    print(solution.letterCombinations(input2))

if __name__ == '__main__':
    main()
