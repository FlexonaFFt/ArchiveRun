class Solution:
    from typing import List
    def maximumSum(self, nums: List[int]) -> int:
        maxSum, left, right = 0, 0, len(nums) - 1
        while left < right:
            counter1, counter2 = 0, 0
            for char in str(nums[left]):
                counter1 += int(char)
            for char in str(nums[right]):
                counter2 += int(char)
            print(counter1)
            print(counter2)

            if counter1 == counter2:
                result = nums[left] + nums[right]
                if maxSum < result:
                    maxSum = result
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1
                continue
        if maxSum == 0:
            return -1
        return maxSum

def main():
    solution = Solution()
    print(solution.maximumSum(nums=[18,43,36,13,7]))
    print(solution.maximumSum(nums=[10,12,19,14]))

if __name__ == '__main__':
    main()
