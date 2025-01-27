class Solution:
    def intToRoman(self, num: int) -> str:
        val = [(1000, "M"), (900, "CM"), (500, "D"),
            (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (10, "X"),
            (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")]

        result = []
        for value, symbol in val:
            while num >= value:
                result.append(symbol)
                num -= value
        return ''.join(result)

# Runtime 5 ms, 55 %
# Memory 18 mb, 17.63 %
def main():
    num1, num2, num3 = 3749, 58, 1994
    solution = Solution()
    print(solution.intToRoman(num1))
    print(solution.intToRoman(num2))
    print(solution.intToRoman(num3))

if __name__ == '__main__':
    main()
