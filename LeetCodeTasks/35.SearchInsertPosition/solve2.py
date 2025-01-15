class Solution:
    from typing import List
    def searchInsert(self, nums: List[int], target: int) -> int:
        closest_number, closest_index = nums[0], 0
        min_distance = abs(nums[0] - target)
        for index, number in enumerate(nums):
            distance = abs(number - target)
            if distance < min_distance:
                min_distance = distance 
                closest_number = number 
                closest_index = index 
        if closest_number < target:
            closest_index += 1
        return closest_index

# Runtime 0 ms, Beast 100 %
def main():
    numbers = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    print(solution.searchInsert(numbers, target))

if __name__ == '__main__':
    main()
