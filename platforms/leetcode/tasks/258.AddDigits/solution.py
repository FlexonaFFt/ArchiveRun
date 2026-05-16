class Solution:
    def addDigits(self, num: int) -> int:
        seen = set()
        while len(str(num)) != 1 and num not in seen:
            seen.add(num)
            digits = [int(char) for char in str(num)]
            num = sum(digit for digit in digits)
        return num

# Runtime 0 ms, 100 %
# Memory 17.65 mb, 72.93 %
def main():
    solve = Solution()
    print(solve.addDigits(num=38))
    print(solve.addDigits(num=0))

if __name__ == '__main__':
    main()
