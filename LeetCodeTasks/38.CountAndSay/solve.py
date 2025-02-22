class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = "1"
        for _ in range(1, n):
            curr = ""
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i-1]:
                    count += 1
                else:
                    curr += str(count) + prev[i-1]
                    count = 1
            curr += str(count) + prev[-1]
            prev = curr

        return prev

# Runtime 7 ms, 75.20 %
# Memory 17.74 mb, 85.30 %
def main():
    solve = Solution()
    print(solve.countAndSay(n=4))
    print(solve.countAndSay(n=1))

if __name__ == '__main__':
    main()
