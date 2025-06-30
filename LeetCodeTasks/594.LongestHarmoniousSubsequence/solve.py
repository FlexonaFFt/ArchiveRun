from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq, max_len = Counter(nums), 0

        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])

        return max_len 

# Runtime 20 ms, 83.87 %
# Memory 19.36 mb, 11.14 %
def test():
    solve = Solution()
    print(solve.findLHS(nums=[1,3,2,2,5,2,3,7]))
    print(solve.findLHS(nums=[1,2,3,4]))
    print(solve.findLHS(nums=[1,1,1,1]))

if __name__ == '__main__':
    test()
