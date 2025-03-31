class Solution:
    def yaGolodny(self, n: int, e:int, s:int) -> float:
        distance = min(abs(e - s), n - abs(e - s))
        expected_time = (n**2 - distance**2) / 4
        return expected_time


def test():
    solution = Solution()
    print(solution.yaGolodny(3, 2, 1))
    print(solution.yaGolodny(4, 1, 3))

def main():
    solution = Solution()
    n, e, s = map(int, input().split())
    print(solution.yaGolodny(n, e, s))

if __name__ == '__main__':
    test()
