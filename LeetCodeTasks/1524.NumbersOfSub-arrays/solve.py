class Solution:
    from typing import List
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount, prefixSum, mod = 0, 0, 1_000_000_007
        for a in arr:
            prefixSum += a
            oddCount += prefixSum % 2
        oddCount += (len(arr) - oddCount) * oddCount
        return oddCount % mod

# Runtime 44 ms, 93.00 %
# Memory 21.98 mb, 42.66 %
def main():
    solve = Solution()
    print(solve.numOfSubarrays(arr=[1,3,5]))
    print(solve.numOfSubarrays(arr=[2,4,6]))
    print(solve.numOfSubarrays(arr=[1,2,3,4,5,6,7]))

if __name__ == '__main__':
    main()
