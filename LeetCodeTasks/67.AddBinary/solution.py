class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = int(a, 2), int(b, 2)
        return str(bin(num1 + num2)[2:])

# Runtime 0 ms, 100 %
# Memory 17.93 mb, 23.73 %
def main():
    solve = Solution()
    a1, b1 = '11', '1'
    a2, b2 = '1010', '1011'
    print(solve.addBinary(a1, b1))
    print(solve.addBinary(a2, b2))

if __name__ == '__main__':
    main()
