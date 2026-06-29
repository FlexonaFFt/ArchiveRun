class Solution:
    from typing import List
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f'{nums[0]}/{nums[1]}'
        denominator = '/'.join(map(str, nums[1:]))
        return f'{nums[0]}/({denominator})'

# Runtime 0 ms, 100 %
# Memory 17.54 mb, 92 %
def main():
    solve = Solution()
    print(solve.optimalDivision(nums=[1000, 100, 10, 2]))
    print(solve.optimalDivision(nums=[2, 3, 4]))

if __name__ == '__main__':
    main()
