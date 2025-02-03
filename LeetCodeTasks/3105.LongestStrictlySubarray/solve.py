class Solution:
    from typing import List
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestCnt, arraysList = 0, {}
        for element in nums:
            if element not in arraysList:
                arraysList[element] = 1
            else:
                arraysList[element] += 1
        for key in arraysList.values():
            if key > longestCnt:
                longestCnt = key
        return longestCnt

# Я не так понял условие задачи, поэтому решение не подходит
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
