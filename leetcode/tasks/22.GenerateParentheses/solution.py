class Solution:
    from typing import List
    def generateParenthesis(self, num: int) -> List[str]:
        def backtrack(current, openCount, closeCount):
            if len(current) == 2 * num:
                result.append(current)
                return
            if openCount < num:
                backtrack(current + "(", openCount + 1, closeCount)
            if closeCount < openCount:
                backtrack(current + ")", openCount, closeCount + 1)

        result = []
        backtrack('', 0, 0)
        return result

# Runtime 0 ms, 100 %
# Memory 17.98 mb, 63.76 %
def main():
    solution = Solution()
    print(solution.generateParenthesis(num=3))
    print(solution.generateParenthesis(num=1))

if __name__ == '__main__':
    main()
