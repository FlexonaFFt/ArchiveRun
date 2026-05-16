class Solution:
    def pitanie(self, n: int, a: int, b: int):
        for x in range(n // a + 1):
            remaining = n - x * a
            if remaining % b == 0:
                y = remaining // b
                print("YES")
                print(x, y)
                exit()
        print("NO")


def main():
    solve = Solution()
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    solve.pitanie(n, a, b)

if __name__ == '__main__':
    main()
