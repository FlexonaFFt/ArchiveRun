class Solution:
    def hammingDistance(self, x: int, y: int):
        xor_result = x ^ y
        distance = bin(xor_result).count('1')
        return distance

# Runtime 0 ms, 100 %
# Memory 17.80 mb, 56.48 %
def main():
    solution = Solution()
    print(solution.hammingDistance(x=1, y=4))
    print(solution.hammingDistance(x=3, y=1))

if __name__ == '__main__':
    main()
