class Solution:
    def docker(self, n: int, way: list[int]) -> int:
        if n < 2 :
            return 0
        max_len = 0


        for i in range(n):
            left = i
            while left > 0 and way[left - 1] <= way[left]:
                left -= 1

            right = i
            while right < n - 1 and way[right + 1] <= way[right]:
                right += 1

            if left < right:
                is_mirror = True
                for j in range((right - left + 1) // 2):
                    if way[left + j] != way[right - j]:
                        is_mirror = False
                        break

                if is_mirror:
                    current_length = right - left + 1
                    if current_length > max_len:
                        max_len = current_length


        return max_len if max_len >= 2 else 0


def test():
    solution = Solution()
    print(solution.docker(7, [1, 2, 3, 4, 3, 2, 1]))
    print(solution.docker(5, [1, 2, 3, 4, 5]))
    print(solution.docker(10, [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]))
    print(solution.docker(3, [1, 1, 2]))
    print(solution.docker(6, [1, 1, 1, 1, 3, 4]))

def main():
    solution = Solution()
    n = int(input())
    way = list(map(int, input().split()))

    print(solution.docker(n=n, way=way))

if __name__ == '__main__':
    test()
