class Solution:
    def findComplement(self, num: int):
        new, binary = '', str(bin(num)[2:])
        for element in binary:
            if element == '0':
                new += ''.join('1')
            elif element == '1':
                new += ''.join('0')
        return int(new, 2)

# Runtime 0 ms, 100 %
# Memory 17.64 mb, 68.48 %
def main():
    solve = Solution()
    print(solve.findComplement(5))

if __name__ == '__main__':
    main()
