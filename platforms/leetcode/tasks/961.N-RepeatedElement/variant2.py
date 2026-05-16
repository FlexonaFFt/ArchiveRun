import collections
class Solution:
    from typing import List
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for key, value in count.items():
            if value > 1:
                return key


def main():
    solve = Solution()
    print(solve.repeatedNTimes([1,2,3,3]))
    print(solve.repeatedNTimes([2,1,2,5,3,2]))
    print(solve.repeatedNTimes([5,1,5,2,5,3,5,4]))

if __name__ == '__main__':
    main()
