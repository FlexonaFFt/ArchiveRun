class Solution:
    from typing import List
    def countBadPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and j - i != nums[j] - nums[i]:
                    counter += 1
        return counter

# Ахереть, я полностью сам написал это решение
# Оно проходит 48 теста, и на 49 вознкиает TL
def main():
    solution = Solution()
    print(solution.countBadPairs([4,1,3,3]))
    print(solution.countBadPairs([1,2,3,4,5]))

if __name__ == '__main__':
    main()
