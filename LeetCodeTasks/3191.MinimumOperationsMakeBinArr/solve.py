class Solution:
    def minOperations(self, nums: list[int]) -> int:
        flip1 = flip2 = False
        n, count = len(nums), 0

        for i in range(n - 2):
            need_fleep = nums[i] == flip1
            flip1, flip2 = flip2, 0
            if need_fleep:
                count += 1
                flip1 = not flip1
                flip2 = True

        return count if nums[n - 2] != flip1 and nums[n - 1] != flip2 else -1

# Runtime 75 ms, 98 %
# Memory 21.67 mb, 54.50 %
def main():
    solve = Solution()
    print(solve.minOperations(nums=[0,1,1,1,0,0]))
    print(solve.minOperations(nums=[0,1,1,1]))

if __name__ == '__main__':
    main()
