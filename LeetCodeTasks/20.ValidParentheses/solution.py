class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        matchedBrackets = {')':'(', '}':'{', ']':'['}
        for char in string:
            if char in matchedBrackets:
                if stack == [] or matchedBrackets[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack

# Runtime 0 ms, 100 %
# Memory 17.95 mb, 28.55 %
def main():
    solve = Solution()
    print(solve.isValid('()'))
    print(solve.isValid('()[]{}'))
    print(solve.isValid('(]'))
    print(solve.isValid('([])'))

if __name__ == '__main__':
    main()
