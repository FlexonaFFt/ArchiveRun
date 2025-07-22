class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        max_sum, current_sum, start = 0, 0, 0
        seen = set()
        for end in range(len(nums)):
            while nums[end] in seen:
                seen.remove(nums[start])
                current_sum -= nums[start]
                start += 1
            seen.add(nums[end])
            current_sum += nums[end]
            if max_sum < current_sum:
                max_sum = current_sum

        return max_sum


def test():
    solve = Solution()
    print(solve.maximumUniqueSubarray(nums=[4,2,4,5,6]))
    print(solve.maximumUniqueSubarray(nums=[5,2,1,2,5,2,1,2,5]))

if __name__ == '__main__':
    test()
