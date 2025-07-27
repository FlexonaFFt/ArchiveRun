class Solution:
    def maxSum(self, nums: list[int]) -> int:
        seen = set()
        left, curr_sum, max_sum = 0, 0, float("-inf")

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            curr_sum += nums[right]
            if max_sum < curr_sum:
                max_sum = curr_sum

        return max_sum


def test():
    solve = Solution()
    print(solve.maxSum([1,2,3,4,5]))
    print(solve.maxSum([1,1,0,1,1]))
    print(solve.maxSum([1,2,-1,-2,1,0,-1]))

if __name__ == '__main__':
    test()
