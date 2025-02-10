class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                while stack and stack[-1].isdigit():
                    stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

# Runtime 0 ms, 100 %
# Memory 17.63 mb, 70 %
def main():
    solve = Solution()
    print(solve.clearDigits('abc'))
    print(solve.clearDigits('ab34'))

if __name__ == '__main__':
    main()
