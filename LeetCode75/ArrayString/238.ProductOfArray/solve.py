class Solution:
    from typing import List
    def ProductExpectSelf(sel, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        prefix_product, suffix_product = [1] * len(nums), [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            product[i] = prefix_product[i] * suffix_product[i]
        return product

# Runtime 35 ms, 27.19 %
# Memory 27.02 mb, 7.60 %
def main():
    nums = list(map(int, input().split()))
    solution = Solution()
    print(solution.ProductExpectSelf(nums=nums))

if __name__ == '__main__':
    main()
