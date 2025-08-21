class Solution:
    def func(self, n: int) -> int:
        digits = list(str(n))
        digits.sort()

        if digits[0] == '0':
            for i in range(1, 4):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break

        result = ''.join(digits)
        return result


def test():
    solve = Solution()
    print(solve.func(7331))  # Ожидается: 1337
    print(solve.func(2017))  # Ожидается: 1027
    print(solve.func(1234))  # Ожидается: 1234
    print(solve.func(4321))  # Ожидается: 1234
    print(solve.func(1009))  # Ожидается: 1009
    print(solve.func(9100))  # Ожидается: 1009
    print(solve.func(1200))  # Ожидается: 1002

def main():
    x = int(input())
    solve = Solution()
    print(solve.func(n=x))

if __name__ == '__main__':
    main()
