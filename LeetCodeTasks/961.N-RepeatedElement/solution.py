import collections
class Solution:
    from typing import List
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for k in count:
            if count[k] > 1:
                return k

# Runtime 13 ms, 25.96 %
# Memory 18.80 mb, 52.68 %
def main():
    solve = Solution()
    print(solve.repeatedNTimes([1,2,3,3]))
    print(solve.repeatedNTimes([2,1,2,5,3,2]))
    print(solve.repeatedNTimes([5,1,5,2,5,3,5,4]))

if __name__ == '__main__':
    main()
