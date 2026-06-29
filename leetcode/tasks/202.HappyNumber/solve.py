class Solution:
    def isHappy(self, n: int) -> bool:
        '''counter, product, string = 0, 0, str(int)
        while product != 1 or counter <= 100000:
            number = string
            digits = [int(char) for char in number]
            product = sum(digit**2 for digit in digits)
            if product == 1:
                return True
        return False'''

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            digits = [int(char) for char in str(n)]
            n = sum(digit**2 for digit in digits)
        return n == 1

# Runtime 3 ms, 43.35 %
# Memory 17.83 mb, 32.99 %
def main():
    solution = Solution()
    print(solution.isHappy(n=19))

if __name__ == '__main__':
    main()
