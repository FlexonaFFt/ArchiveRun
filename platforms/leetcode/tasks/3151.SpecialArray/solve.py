class Solution:
    from typing import List
    def isArraySpecial(self, nums: List[int]):
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            if (nums[i] % 2) == (nums[i + 1] % 2):
                return False
        return True

# Runtime 0 ms, 100 %
# Memory 18.05 mb, 12.54 %
def main():
    solve = Solution()
    primer1, primer2 = [1], [2, 1, 4]
    primer3 = [4, 3, 1, 6]
    print(solve.isArraySpecial(primer1))
    print(solve.isArraySpecial(primer2))
    print(solve.isArraySpecial(primer3))

if __name__ == '__main__':
    main()
