class Solution:
    from typing import List
    def lengthOfLIS(self, nums: List[int]):
        if not nums:
            return 0

        answer, minEl, maxEl = [], min(nums), max(nums)
        answer.append(minEl)
        idx = nums.index(minEl)
        for i in range(idx, len(nums)):
            if nums[i - 1] < nums[i]:
                answer.append(nums[i])
            if nums[i] == maxEl:
                break
        return len(answer), answer

# Test 29, 27
def main():
    solution = Solution()
    print(solution.lengthOfLIS(nums=[10,9,2,5,3,7,101,18]))
    print(solution.lengthOfLIS(nums=[0,1,0,3,2,3]))
    print(solution.lengthOfLIS(nums=[7,7,7,7,7,7,7]))
    print(solution.lengthOfLIS(nums=[1,3,6,7,9,4,10,5,6]))
    print(solution.lengthOfLIS(nums=[0,1,0,3,2,3]))

if __name__ == '__main__':
    main()
