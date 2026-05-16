class Solution:
    def docker(self, n: int, way: list[int]) -> int:
        if n < 2 :
            return 0
        max_len = 0


        for i in range(n):
            left, right = i, i
            while left > 0 and way[left - 1] < way[left]:
                left -= 1
            while right < n - 1 and way[right + 1] < way[right]:
                right += 1

            if left < i < right:
                curr_len = right - left + 1
                max_len = max(max_len, curr_len)

        return max_len if max_len >= 2 else 0


def main():
    solution = Solution()
    n = int(input())
    way = list(map(int, input().split()))

    print(solution.docker(n=n, way=way))

if __name__ == '__main__':
    main()
