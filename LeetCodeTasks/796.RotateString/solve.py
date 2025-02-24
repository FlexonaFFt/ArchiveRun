class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False

# Runtime 3 ms, 100 %
# Memory 17.97 mb, 9.24 %
def main():
    solve = Solution()
    print(solve.rotateString(s="abcde", goal="cdeab"))
    print(solve.rotateString(s="abcde", goal="abced"))

if __name__ == '__main__':
    main()
