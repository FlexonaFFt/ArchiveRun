from collections import defaultdict
class Solution:
    def solveFunction(self, n: int, k: int, confs: list[int]) -> int:
        if k == 1:
            return 1

        unique_count = defaultdict(int)
        for i in range(k):
            unique_count[confs[i]] += 1

        max_unique = len(unique_count)
        for i in range(k, n):
            unique_count[confs[i]] += 1
            unique_count[confs[i - k]] -= 1
            if unique_count[confs[i - k]] == 0:
                del unique_count[confs[i - k]]

            max_unique = max(max_unique, len(unique_count))

        return max_unique

def test():
    solve = Solution()
    print(solve.solveFunction(n=10, k=4, confs=[4, 42, 42, 42, 2, 3, 42, 2, 3, 2]))

def main():
    solve = Solution()
    n, k = map(int, input().split())
    spisok = list(map(int, input().split()))
    print(solve.solveFunction(n, k, spisok))

if __name__ == '__main__':
    main()
