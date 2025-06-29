class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % mod 

        left, right = 0, n - 1
        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % mod 
                left += 1
            else: right -= 1

        return result 

# Runtime 112 ms, 95.24 %
# Memory 27.77 mb, 78.60 %
def test():
    solve = Solution()
    print(solve.numSubseq(nums=[3,5,6,7], target=9))
    print(solve.numSubseq(nums=[3,3,6,8], target=10))
    print(solve.numSubseq(nums=[2,3,3,4,6,7], target=12))

if __name__ == '__main__': 
    test()
