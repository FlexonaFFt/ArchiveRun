class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        from itertools import permutations
        unique_numbers = set()
        for i, last_digit in enumerate(digits):
            if last_digit % 2 == 0:
                remaining_digits = digits[:i] + digits[i+1:]

                for p in permutations(remaining_digits, 2):
                    if p[0] != 0:
                        number = p[0] * 100 + p[1] * 10 + last_digit
                        unique_numbers.add(number)

        return len(unique_numbers)


def main():
    solve = Solution()
    print(solve.totalNumbers([1,2,3,4]))
    print(solve.totalNumbers([0,2,2]))
    print(solve.totalNumbers([6,6,6]))
    print(solve.totalNumbers([1,3,5]))

if __name__ == '__main__':
    main()
