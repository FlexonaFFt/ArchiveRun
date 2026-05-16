class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result, stack = [], []
        for i in range(9, 0, -1):
            if i <= n: stack.append(i)

        while stack:
            current = stack.pop()
            result.append(current)
            for i in range(9, -1, -1):
                next_num = current * 10 + i
                if next_num <= n:
                    stack.append(next_num)

        return result

# Runtime 51 ms, 26.62 %
# Memory 21.28 mb, 77.82 %
def main():
    solve = Solution()
    print(solve.lexicalOrder(n=13))
    print(solve.lexicalOrder(n=2))

if __name__ == '__main__': main()
