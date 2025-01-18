class Solution:
    from typing import List 
    def maxOperations(self, nums: List[int], k: int) -> int: 
        left, right, counter = 0, len(nums) - 1, 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                counter += 1
            elif nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
        return counter 


# Runtime 519 ms, 28.38 % 
# Memory 29.91 mb, 50.20 %
def main():
    numbers, k = [1,2,3,4], 5
    solution = Solution()
    print(solution.maxOperations(nums=numbers, k=k))

if __name__ == '__main__':
    main()
