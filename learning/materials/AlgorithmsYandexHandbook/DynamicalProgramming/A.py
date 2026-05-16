class Solution:
    def FastRocks(self, n: int, m: int) -> str:
        if n % 2 == 0 and m % 2 == 0:
            return 'Lose'
        else:
            return "Win"


def main():
    solve = Solution()
    n, m = map(int, input().split())
    print(solve.FastRocks(n=n, m=m))

if __name__ == '__main__':
    main()
