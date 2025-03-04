class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            rm = n % 3
            if rm == 2:
                return False
            n //= 3
        return True

# Runtime 0 ms, 100 %
# Memory 17.88 mb, 38.84 %
def main():
    solution = Solution()
    print(solution.checkPowersOfThree(n=12))
    print(solution.checkPowersOfThree(n=91))
    print(solution.checkPowersOfThree(n=21))

if __name__ == '__main__':
    main()
