class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        res, n = [], len(nums)

        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break
        return res

# Runtime 123 ms, 42.63 %
# Memory 18.19 mb, 27.63 %
def main():
    solve = Solution()
    print(solve.findKDistantIndices(nums=[3,4,9,1,3,9,5], key=9, k=1))
    print(solve.findKDistantIndices(nums=[2,2,2,2,2], key=2, k=2))


if __name__ == '__main__': main()
