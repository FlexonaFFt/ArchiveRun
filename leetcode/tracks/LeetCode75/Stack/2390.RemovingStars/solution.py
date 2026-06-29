class Solution:
    def removeStars(self, string: str) -> str:
        stack = []
        for char in string:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

# Runtime 95 ms, 67.83 %
# Memory 19.02 mb, 40.33 %
def main():
    solution = Solution()
    string1 = "leet**cod*e"
    string2 = "erase*****"
    print(solution.removeStars(string1))
    print(solution.removeStars(string2))

if __name__ == '__main__':
    main()
