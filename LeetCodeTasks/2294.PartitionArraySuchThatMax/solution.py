class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        current, answer = nums[0], 1

        for num in nums:
            if num - current > k:
                answer += 1
                current = num
        return answer

# Runtime 75 ms, 92.99 %
# Memory 29.08 mb, 73.61 %
def test():
    solve = Solution()
    print(solve.partitionArray(nums=[3,6,1,2,5], k=2))
    print(solve.partitionArray(nums=[1,2,3], k=1))
    print(solve.partitionArray(nums=[2,2,4,5], k=0))

if __name__ == '__main__': test()
