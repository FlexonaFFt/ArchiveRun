class Solution:
    def sumOfGoodNumbers(self, nums, k):
        total_sum = 0
        n = len(nums)
        for i in range(n):
            is_good = True
            if i - k >= 0:
                if nums[i] <= nums[i - k]:
                    is_good = False
            if i + k < n:
                if nums[i] <= nums[i + k]:
                    is_good = False
            if is_good:
                total_sum += nums[i]
        return total_sum

# Runtime 0 ms, 100 %
# Memory 17.72 mb, 82.84 %
def main():
    solution = Solution()
    print(solution.sumOfGoodNumbers(nums=[1,3,2,1,5,4], k=2))
    print(solution.sumOfGoodNumbers(nums=[2,1], k=1))

if __name__ == '__main__':
    main()
