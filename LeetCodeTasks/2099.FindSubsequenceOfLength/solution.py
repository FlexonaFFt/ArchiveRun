class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
        top_k = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]
        top_k_sorted = sorted(top_k, key=lambda x: x[1])
        return [num for num, idx in top_k_sorted]

# Runtime 3 ms, 83.73 %
# Memory 18.02 mb, 54.89 %
def test():
    solve = Solution()
    print(solve.maxSubsequence(nums=[2,1,3,3], k=2))
    print(solve.maxSubsequence(nums=[-1,-2,3,4], k=3))
    print(solve.maxSubsequence(nums=[3,4,3,3], k=2))

if __name__ == '__main__': test()
