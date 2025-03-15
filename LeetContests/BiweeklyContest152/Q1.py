class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        from itertools import permutations
        even_digits = [d for d in digits if d % 2 == 0]
        unique_numbers = set()

        for last_digit in even_digits:
            remaining_digits = [d for d in digits if d != last_digit]
            for first_digit in remaining_digits:
                if first_digit == 0:
                    continue
                second_digit_candidates = [d for d in remaining_digits if d != first_digit]

                for second_digit in second_digit_candidates:
                    number = first_digit * 100 + second_digit * 10 + last_digit
                    unique_numbers.add(number)

        return len(unique_numbers)


def main():
    solve = Solution()
    print(solve.totalNumbers([1,2,3,4]))
    print(solve.totalNumbers([0,2,2]))
    print(solve.totalNumbers([6,6,6]))

if __name__ == '__main__':
    main()
