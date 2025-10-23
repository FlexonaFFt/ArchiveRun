class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        digits = [int(ch) for ch in s]
        while len(digits) > 2:
            next_digits = []
            for i in range(len(digits) - 1):
                next_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = next_digits
        return digits[0] == digits[1]


def test():
    solve = Solution()
    print(solve.hasSameDigits("3902"))
    print(solve.hasSameDigits("34789"))

if __name__ == '__main__':
    test()
