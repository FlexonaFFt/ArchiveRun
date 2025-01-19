class Solution:
    from typing import List
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum / k

# Runtime 38 ms, 96.83 %
# Memory 27.37 mb, 44.16 %
def main():
    array, k = [1,12,-5,-6,50,3], 4
    solution = Solution()
    print(solution.findMaxAverage(array, k))

if __name__ == '__main__':
    main()
