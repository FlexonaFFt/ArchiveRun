class Solution:
    from typing import List
    def check(self, nums: List[int]) -> bool:
        counter = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                counter += 1
        if counter > 1:
            return False
        if counter == 1:
            return nums[-1] <= nums[0]
        return True

# Runtime 0 ms, 100 %
# Memory 17.85 mb, 30 %
def main():
    solve = Solution()
    nums = [3,4,5,1,2]
    nums2 = [2,1,3,4]
    nums3 = [1,2,3]
    print(solve.check(nums))
    print(solve.check(nums2))
    print(solve.check(nums3))

if __name__ == '__main__':
    main()
