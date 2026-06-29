class Solution:
    from typing import List
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

# Runtime 0 ms, 100 %
# Memory 17.95 mb, 82.94 %
def main():
    solution = Solution()
    nums, num = [4,5,6,7,0,1,2], [1]
    target1, target2 = 0, 3
    print(solution.search(nums=nums, target=target1))
    print(solution.search(nums=nums, target=target2))
    print(solution.search(nums=num, target=target1))

if __name__ == '__main__':
    main()
