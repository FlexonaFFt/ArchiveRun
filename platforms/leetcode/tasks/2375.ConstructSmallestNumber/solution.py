class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result, stack, num = [], [], 1
        for char in pattern:
            stack.append(str(num))
            num += 1
            if char == 'I':
                while stack:
                    result.append(stack.pop())
        stack.append(str(num))
        while stack:
            result.append(stack.pop())
        return ''.join(result)

# Runtime 0 ms, 100 %
# Memory 17.65 mb, 83.23 %
def main():
    solution = Solution()
    print(solution.smallestNumber("IIIDIDDD"))
    print(solution.smallestNumber("DDD"))
    print(solution.smallestNumber("IDID"))
    print(solution.smallestNumber("I"))
    print(solution.smallestNumber("D"))

if __name__ == "__main__":
    main()
