class Solution:
    from typing import List
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        current_inc_len = 1
        current_dec_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_inc_len += 1
                current_dec_len = 1
            elif nums[i] < nums[i - 1]:
                current_inc_len = 1
                current_dec_len += 1
            else:
                current_inc_len = 1
                current_dec_len = 1

        max_len = max(max_len, current_inc_len, current_dec_len)
        return max_len

# Решение не проходит 433 тест sad.
def main():
    solve = Solution()
    primer1 = [1,4,3,3,2]
    primer2 = [3,3,3,3]
    primer3 = [3,2,1]
    print(solve.longestMonotonicSubarray(primer1))
    print(solve.longestMonotonicSubarray(primer2))
    print(solve.longestMonotonicSubarray(primer3))

if __name__ == '__main__':
    main()
