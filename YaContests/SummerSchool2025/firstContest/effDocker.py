class Solution:
    def docker(self, n: int, way: list[int]) -> int:
        if n == 0:
            return 0

        max_len, curr_len, i = 0, 1, 0
        while i < n - 1:
            if way[i] < way[i + 1]:
                curr_len += 1
                i += 1
            else: break

        if curr_len == 1:
            return 0

        while i < n - 1:
            if way[i] > way[i + 1]:
                curr_len += 1
                i += 1
            else: break

        max_len = max(max_len, curr_len)
        return max_len if max_len >= 2 else 0


def main():
    solution = Solution()
    n = int(input())
    way = list(map(int, input().split()))

    print(solution.docker(n=n, way=way))

if __name__ == '__main__':
    main()
