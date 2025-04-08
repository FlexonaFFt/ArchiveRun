class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total, n = 0, len(nums)
        for mask in range(1 << n):
            xor = 0
            for i in range(n):
                if mask & (1 << i):
                    xor ^= nums[i]
            total += xor
        return total


def main():
    solution = Solution()
    print(solution.subsetXORSum([1,3]))
    print(solution.subsetXORSum([5,1,6]))
    print(solution.subsetXORSum([3,4,5,6,7,8]))

main()
