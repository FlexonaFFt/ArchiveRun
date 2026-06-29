class Solution:
    from typing import List
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result, start = [], nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f'{start}->{nums[i - 1]}')
                start = nums[i]

        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f'{start}->{nums[-1]}')
        return result

# Runtime 0 ms, 100 %
# Memory 17.62 mb, 66.95 %
def main():
    solve = Solution()
    primer1 = [0,1,2,4,5,7]
    primer2 = [0,2,3,4,6,8,9]
    print(solve.summaryRanges(primer1))
    print(solve.summaryRanges(primer2))

if __name__ == '__main__':
    main()
